
class Sequence():
    def __init__(self, points):
        points.sort()
        longest_sequences = []
        self.marks = []
        best = (((0, 0), 0, 0), -1)
        for i in range(len(points)):
            longest_sequences_til_i = []
            for j in range(i):
                delta = Sequence.vector(points[i], points[j])
                # search for sequence with difference delta
#               print('liczę', i, j)
                appended = False
                for seq in longest_sequences[j]:
                    if Sequence.fuzzyEqual(seq[0], delta):
                        print(Sequence.vector(seq[0], delta))
                        # can extend sequence
#                       print('przedłużone')
                        longest_sequences_til_i.append((delta, j, seq[2] + 1))
                        appended = True

                if not appended:
#                   print('nowe')
                    longest_sequences_til_i.append((delta, j, 2))

                if best[0][2] < longest_sequences_til_i[-1][2]:
                    best = (longest_sequences_til_i[-1], i)

            longest_sequences.append(longest_sequences_til_i)

#       for row in longest_sequences:
#           print(row)

        current = best[1]
        if current == -1:
            self.marks = []
            return

        self.marks.append(points[current])
        while True:
            entry = None
            for seq in longest_sequences[current]:
                if Sequence.fuzzyEqual(seq[0], best[0][0]):
                    print(Sequence.vector(seq[0], best[0][0]))
                    entry = seq
                    break

            if entry is None:
                break

            current = entry[1]
            self.marks.append(points[current])

        self.marks.reverse()
        print(len(self.marks))


    @staticmethod
    def vector(point1, point2):
        return (point2[0] - point1[0], point2[1] - point1[1])

    def fuzzyEqual(point1, point2):
        EPS = 25
        return abs(point2[0] - point1[0]) < EPS and abs(point2[1] - point1[1]) < EPS


if __name__ == '__main__':
    points = [(128, 470), (43, 390), (38, 380), (73, 346), (120, 342), (95, 236), (95, 236), (165, 338), (136, 232),
              (136, 232), (175, 228), (175, 228), (215, 224), (215, 224), (254, 220), (254, 220), (432, 296),
              (293, 216), (293, 216), (5, 196), (127, 101), (128, 101), (153, 95), (153, 95), (465, 87), (284, 84),
              (284, 84), (413, 73), (413, 73), (541, 62), (541, 62)]

    points1 = [(0, 0), (20, 30), (30, 10), (60, 20), (80, 10), (90, 30)]
    seq = Sequence(points)
    print(seq.marks)
