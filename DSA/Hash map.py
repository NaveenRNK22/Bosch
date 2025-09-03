class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]  

    def hash_function(self, key):
       
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return numeric_sum % 10  
    def put(self, key, value):
        
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  
                return
        bucket.append((key, value))  

    def get(self, key):

        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None  

    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  
                return

    def print_map(self):
        
        print("Hash Map Contents:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")


hash_map = HashMap(size=10)

hash_map.put("001", "Vinesh")
hash_map.put("002", "Sujan")
hash_map.put("003", "Rogith")
hash_map.put("004", "Naveen")

hash_map.print_map()

print("\nName associated with '002':", hash_map.get("002"))

hash_map.remove("004")
hash_map.print_map()