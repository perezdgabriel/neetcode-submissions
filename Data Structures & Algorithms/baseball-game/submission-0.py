class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == '+':
                if len(record) > 1:
                    record.append(record[-2] + record[-1])
            elif op == 'D':
                record.append(2 * record[-1])
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))
        return sum(record)
        