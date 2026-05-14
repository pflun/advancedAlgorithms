# Your task is to write a program that matches incoming payments to their corresponding invoices based on the payment's memo line. An example input string for a payment looks like this:
# payment="paymentABC,500,Paying off: invoiceC", invoices=["invoiceA,2024-01-01,100", "invoiceB,2024-02-01,200", "invoiceC,2023-01-30,1000"]
# (Payment Format) Each comma-separated element represents a different piece of information about the payment:1. The payment ID (e.g. payment123) 2. The payment amount (in USD minor units e.g. $1.00 = 100)
# 3. The memo line, which always follows the format "Paying off: {INVOICE}" (Invoices format) Each comma-separated element represents a different piece of information about the payment:
# 1. The invoice ID 2. The due-date for that invoice 3. The amount due on the invoice (in USD minor units e.g. $1.00 = 100)
# Example input: f("payment5,1000,Paying off: invoiceC", ["invoiceA,2024-01-01,100", "invoiceB,2024-02-01,200", "invoiceC,2023-01-30,1000"])
# Should return: payment5 pays off 1000 for invoiceC due on 2023-01-30
# Followup question:
# f("pid123,500,Bank Transaction", ["invoiceA,2024-01-01,500", "invoiceB,2024-02-01,500"])
# output: pid123 pays off 500 for invoiceA due on 2024-01-01
# Match the payment amount with the invoiceAmount. If multiple invoice has same amount, the return the output with the invoice with earliest due date.
class Solution(object):
    def paymentInvoiceMatching(self, payment, invoices):
        invoice_dic = {}
        for invoice in invoices:
            invoice_id, due_date, amount = invoice.split(",")
            invoice_dic[invoice_id] = [due_date, amount]
        payment_id, amount, memo = payment.split(",")
        memo_invoice_id = memo.split(": ")[1]
        return "{} payoff {} for {} due on {}".format(payment_id, amount, memo_invoice_id, invoice_dic[memo_invoice_id][0])

test = Solution()
print test.paymentInvoiceMatching("paymentABC,500,Paying off: invoiceC", ["invoiceA,2024-01-01,100", "invoiceB,2024-02-01,200", "invoiceC,2023-01-30,1000"])
print test.paymentInvoiceMatching("payment5,1000,Paying off: invoiceC", ["invoiceA,2024-01-01,100", "invoiceB,2024-02-01,200", "invoiceC,2023-01-30,1000"])