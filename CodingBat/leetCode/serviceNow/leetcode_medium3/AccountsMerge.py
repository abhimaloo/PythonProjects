from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

        # Step 1: Connect emails using union-find
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                uf.union(first_email, email)
                email_to_name[email] = name

        # Step 2: Group emails by parent
        groups = defaultdict(list)
        for email in email_to_name:
            parent = uf.find(email)
            groups[parent].append(email)

        # Step 3: Format the result
        result = []
        for parent, emails in groups.items():
            name = email_to_name[parent]
            result.append([name] + sorted(emails))

        return result


"""
 Key Idea:
Use Union-Find (Disjoint Set) to connect emails that belong to the same person.

Each email points to its owner’s name and is connected via union operations.

✅ Step-by-Step Plan:
Use Union-Find to group emails.

Map each email to a name.

For each group (connected component), collect and sort emails.


✅ Time and Space Complexity
Metric	Complexity
Time	O(N * α(N)) + N log N

N = total number of emails

α(N) = inverse Ackermann function (very small)
| Space | O(N) — for maps and Union-Find storage |



"""