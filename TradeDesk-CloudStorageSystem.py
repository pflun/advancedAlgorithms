# -*- coding: utf-8 -*-
# Level 1
# from cloud_storage import CloudStorage
class CloudStorage(object):
    pass

class CloudStorageImpl(CloudStorage):
    def __init__(self):
        # Maps file_name (str) -> size (int)
        self.files = {}

    def add_file(self, name, size):
        if name in self.files:
            return False
        self.files[name] = size
        return True

    def copy_file(self, name_from, name_to):
        # Check if source exists and destination is available
        if name_from not in self.files or name_to in self.files:
            return False

        # Copy the size to the new path
        self.files[name_to] = self.files[name_from]
        return True

    def get_file_size(self, name):
        # Returns size if exists, otherwise None
        return self.files.get(name)

# Level 2

class CloudStorageImpl2(CloudStorage):
    def __init__(self):
        self.files = {}

    def find_file(self, prefix, suffix):
        matches = []

        # 1. Filter files based on prefix and suffix
        for name, size in self.files.items():
            if name.startswith(prefix) and name.endswith(suffix):
                matches.append((name, size))

        # 2. Sort the matches
        # We use -x[1] for descending size, and x[0] for ascending name
        matches.sort(key=lambda x: (-x[1], x[0]))

        # 3. Format the output strings
        return ["{0}({1})".format(name, size) for name, size in matches]

# Level 3

class CloudStorageImpl3(CloudStorage):
    def __init__(self):
        self.files = {}        # name -> size
        self.file_owners = {}  # name -> user_id
        self.users = {
            "admin": {"capacity": float('inf'), "usage": 0}
        }

    def add_user(self, user_id, capacity):
        if user_id in self.users:
            return False
        self.users[user_id] = {"capacity": capacity, "usage": 0}
        return True

    def add_file(self, name, size):
        # Level 1 inherited: admin calls this
        return self.add_file_by("admin", name, size) is not None

    def add_file_by(self, user_id, name, size):
        if user_id not in self.users or name in self.files:
            return None

        user = self.users[user_id]
        if user["usage"] + size > user["capacity"]:
            return None

        # Register file and update usage
        self.files[name] = size
        self.file_owners[name] = user_id
        user["usage"] += size
        return user["capacity"] - user["usage"]

    def copy_file(self, name_from, name_to):
        if name_from not in self.files or name_to in self.files:
            return False

        owner_id = self.file_owners[name_from]
        size = self.files[name_from]
        user = self.users[owner_id]

        # Check if owner has room for a duplicate
        if user["usage"] + size > user["capacity"]:
            return False

        self.files[name_to] = size
        self.file_owners[name_to] = owner_id
        user["usage"] += size
        return True

    def update_capacity(self, user_id, capacity):
        if user_id not in self.users:
            return None

        user = self.users[user_id]
        user["capacity"] = capacity
        removed_count = 0

        if user["usage"] > capacity:
            # Get all files belonging to this user
            user_files = [
                (name, size) for name, size in self.files.items()
                if self.file_owners[name] == user_id
            ]

            # Sort: Largest size first, then lexicographical name for ties
            # Note: The prompt says "largest files... (lexicographically in case of a tie)"
            # This implies the same sort logic as find_file: (-size, name)
            user_files.sort(key=lambda x: (-x[1], x[0]))

            for name, size in user_files:
                if user["usage"] <= capacity:
                    break

                # Delete the file
                del self.files[name]
                del self.file_owners[name]
                user["usage"] -= size
                removed_count += 1

        return removed_count

    # Keep your find_file and get_file_size from previous levels...

# Level 4

class CloudStorageImpl4(CloudStorage):
    def __init__(self):
        self.files = {}
        self.file_owners = {}
        self.users = {
            "admin": {"capacity": float('inf'), "usage": 0}
        }

    def compress_file(self, user_id, name):
        # Check if file exists and user owns it
        if name not in self.files or self.file_owners.get(name) != user_id:
            return None

        # New file properties
        new_name = name + ".COMPRESSED"
        old_size = self.files[name]
        new_size = old_size // 2

        # Remove old file and add new one
        del self.files[name]
        # Note: file_owners needs update if we delete name
        self.file_owners[new_name] = self.file_owners.pop(name)
        self.files[new_name] = new_size

        # Update user usage (size decreased by half)
        user = self.users[user_id]
        user["usage"] -= (old_size - new_size)

        return user["capacity"] - user["usage"]

    def decompress_file(self, user_id, name):
        # 1. Verification: name must exist and be owned by user
        if name not in self.files or self.file_owners.get(name) != user_id:
            return None

        # 2. Name logic: name always ends in .COMPRESSED
        original_name = name.replace(".COMPRESSED", "")

        # 3. Collision check: original name must be free
        if original_name in self.files:
            return None

        current_size = self.files[name]
        original_size = current_size * 2
        size_increase = original_size - current_size

        user = self.users[user_id]

        # 4. Capacity check
        if user["usage"] + size_increase > user["capacity"]:
            return None

        # 5. Commit changes
        del self.files[name]
        self.file_owners[original_name] = self.file_owners.pop(name)
        self.files[original_name] = original_size
        user["usage"] += size_increase

        return user["capacity"] - user["usage"]
