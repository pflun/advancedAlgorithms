# -*- coding: utf-8 -*-

class Worker(object):
    def __init__(self, worker_id, position, compensation):
        self.id = worker_id
        self.position = position
        self.compensation = compensation
        
        # Level 3: Promotions take effect on the NEXT visit. 
        # We store them as pending until the worker enters the office again.
        self.pending_position = None
        self.pending_compensation = None
        
        # If None, the worker is currently outside. Otherwise, it stores the entry timestamp.
        self.entry_time = None
        
        # Stores historical sessions as tuples: (start, end, position_during_session, comp_during_session)
        self.finished_sessions = []

class WorkerSystem(object):
    def __init__(self):
        # Maps worker_id (str) -> Worker object
        self.workers = {}
        # Stores registered grant periods as a dictionary: (start_timestamp, end_timestamp) -> True
        self.grants = {}

    # --- LEVEL 1 ---

    def add_worker(self, worker_id, position, compensation):
        if worker_id in self.workers:
            return False
        self.workers[worker_id] = Worker(worker_id, position, compensation)
        return True

    def register(self, worker_id, timestamp):
        if worker_id not in self.workers:
            return "invalid_request"
        
        worker = self.workers[worker_id]
        
        if worker.entry_time is None:
            # Worker is entering the office.
            # Level 3 requirement: apply any pending promotion for this new session.
            if worker.pending_position is not None:
                worker.position = worker.pending_position
                worker.compensation = worker.pending_compensation
                worker.pending_position = None
                worker.pending_compensation = None
            
            worker.entry_time = timestamp
        else:
            # Worker is leaving the office. Record the completed session.
            worker.finished_sessions.append((
                worker.entry_time, 
                timestamp, 
                worker.position, 
                worker.compensation
            ))
            worker.entry_time = None
            
        return "registered"

    def get(self, worker_id):
        if worker_id not in self.workers:
            return None
        worker = self.workers[worker_id]
        # Only count completed sessions
        return sum(end - start for start, end, _, _ in worker.finished_sessions)


    # --- LEVEL 2 ---

    def top_n_workers(self, n, position):
        valid_workers = []
        for worker in self.workers.values():
            if worker.position == position:
                total_time = sum(end - start for start, end, _, _ in worker.finished_sessions)
                valid_workers.append((worker.id, total_time))
        
        # Sort descending by total time (-x[1]), then ascending alphabetically by id (x[0])
        valid_workers.sort(key=lambda x: (-x[1], x[0]))
        
        # Take top n (if valid_workers has fewer than n, slicing naturally handles it)
        valid_workers = valid_workers[:n]
        
        return ["{0}({1})".format(wid, time) for wid, time in valid_workers]


    # --- LEVEL 3 ---

    def promote(self, worker_id, new_position, new_compensation):
        if worker_id not in self.workers:
            return "invalid_request"
        
        worker = self.workers[worker_id]
        # Last request overrides any previous pending requests.
        worker.pending_position = new_position
        worker.pending_compensation = new_compensation
        
        return "success"

    def calc_salary(self, worker_id, start_timestamp, end_timestamp):
        if worker_id not in self.workers:
            return None
        
        worker = self.workers[worker_id]
        total_salary = 0
        
        for s_start, s_end, pos, comp in worker.finished_sessions:
            # Calculate the intersection between the query period and the session
            overlap_start = max(s_start, start_timestamp)
            overlap_end = min(s_end, end_timestamp)
            
            if overlap_start < overlap_end:
                multiplier = 1
                
                # Level 4 requirement: check if the session is fully contained within ANY registered grant
                for g_start, g_end in self.grants.keys():
                    if s_start >= g_start and s_end <= g_end:
                        multiplier = 2
                        break
                
                # Multiply intersection duration by historical compensation and multiplier
                total_salary += (overlap_end - overlap_start) * comp * multiplier
                
        return total_salary


    # --- LEVEL 4 ---

    def register_grant(self, start_timestamp, end_timestamp):
        self.grants[(start_timestamp, end_timestamp)] = True

    def get_grant_bonus(self, start_timestamp, end_timestamp):
        grant_key = (start_timestamp, end_timestamp)
        if grant_key not in self.grants:
            return 0
        
        bonus = 0
        for worker in self.workers.values():
            for s_start, s_end, pos, comp in worker.finished_sessions:
                # Check if session is exactly fully contained within THIS specific grant period
                if s_start >= start_timestamp and s_end <= end_timestamp:
                    # The bonus is the difference between 2x and 1x pay (which is exactly 1x base pay)
                    bonus += (s_end - s_start) * comp
                    
        return bonus
