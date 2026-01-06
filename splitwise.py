class SplitWise:
    def solution (self):
        payment_summary={
            "hari":1200,
            "vipin":1400,
            "jhon" :1000,
            "vishnu":0,
            "tom" : 120,
            "avinash":0,
            "jinu":0,
            "asok":0
    }
        #step 1 calculate total_expense
        total = sum(payment_summary.values())
        print("total expense",total)
        # step 2 calculate indivual split
        individual_split= total/len(payment_summary)
        result={k:individual_split-v for k,v in payment_summary.items()}
        print("amount:",result)
split_instance=SplitWise()
split_instance.solution()
