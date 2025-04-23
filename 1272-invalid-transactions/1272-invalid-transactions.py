class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # hash-map and invalid
        hash_map = defaultdict(list)
        invalid = set()
        
        # iterate through transactions
        for ind , transaction in enumerate(transactions):
            # unpack the name,amount,time ,city from each element
            name, time , amount , city = transaction.split(",")
            time , amount = int(time) ,int(amount)
            # store them on hash-map (name: [time,amount,city])
            hash_map[name].append([time,city, ind])

            # check the amount for each transaction and mark them invalid if the are greate than 1000
            if amount > 1000:
                invalid.add(ind)
            # check the second rule for all transaction that have same name
            for t , c , j in hash_map[name]:
                if c != city and abs(time-t) <= 60:
                    invalid.add(ind)
                    invalid.add(j)
        #return all the invalid transaction by iterate on invalid set

        return [transactions[i] for i in invalid]