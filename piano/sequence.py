import numpy as np


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, alpha):
        return Point(self.x * alpha, self.y * alpha)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        EPS = 5
        return abs(other.x - self.x) <= EPS and abs(other.y - self.y) <= EPS


class Sequence():
    def __init__(self, points):
        points.sort()
        points = [Point(x, y) for (x, y) in points]
        longest_sequences = []
        self.marks = []

        class Entry():
            def __init__(self, delta=None, prev=None, length=0, last_id=None):
                self.delta = delta
                self.prev = prev
                self.length = length
                self.last_id = last_id

            def __lt__(self, other):
                return self.length < other.length

        best = None

        for i, p in enumerate(points):
            sequences_i = []            

            for j, q in enumerate(points[:i]):
                # for every previous point q try to extend sequence 
                # by p with delta q - p

                delta = q - p

                # search for difference with difference delta
                # ending in point q (with id j)
                sequence_ij = None
                for k in range(1, 3):
                    for seq in longest_sequences[j]:
                        # first sequence will be chosen (should we minimize error when comparing?)
                        # should we choose the longest entry instead of the smallest k first
                        if seq.delta * k == delta and sequence_ij is None:  # Sequence.fuzzyEqual(seq[0], delta, k) and not appended:
                            # sequence can be extended
                            # TODO new entry delta should be delta (new) or seq.delta (old)?
                            sequence_ij = Entry(seq.delta, seq, seq.length + 1, i)

                if sequence_ij is None:
                    # if no sequence can be extended create new one consisting of points i and j
                    prev_entry = Entry(None, None, 1, j)
                    sequence_ij = Entry(delta, prev_entry, 2, i)

                if best is None or best < sequence_ij:
                    best = sequence_ij

                sequences_i.append(sequence_ij)

            longest_sequences.append(sequences_i)

#       print(best.delta, best.length)

        self.marks = []
        while best is not None:
            self.marks.append(points[best.last_id])
            best = best.prev
    
        self.marks.reverse()


#       for i, p in enumerate(points):
#           longest_sequences_til_i = []
#           for j in range(i):
#               delta = Sequence.vector(points[i], points[j])
#               # search for sequence with difference delta
#               appended = False
#               # TODO Sometimes algorithm chooses not smallest possible delta and misses some points of valid sequence
#               for k in range(1, 5):
#                   for seq in longest_sequences[j]:
#                       if Sequence.fuzzyEqual(seq[0], delta, k) and not appended:
#                           # can extend sequence
#                           longest_sequences_til_i.append((seq[0], j, seq[2] + 1))
#                           appended = True
#                           print('appended', k, delta)

#               if not appended:
#                   longest_sequences_til_i.append((delta, j, 2))

#               if best[0][2] < longest_sequences_til_i[-1][2]:
#                   best = (longest_sequences_til_i[-1], i)

#           longest_sequences.append(longest_sequences_til_i)

#       print('retrieving best sequence')
#       current = best[1]
#       if current == -1:
#           self.marks = []
#           return

#       self.marks.append(points[current])
#       while True:
#           entry = None
#           for seq in longest_sequences[current]:
#               if Sequence.fuzzyEqual(seq[0], best[0][0]):
#                   entry = seq
#                   break

#           if entry is None:
#               break

#           current = entry[1]
#           self.marks.append(points[current])

#       self.marks.reverse()

#       print("filling the gaps")
#       self.marks = Sequence.fillGaps(self.marks, best[0][0])

    @staticmethod
    def fillGaps(points, delta):
        filled_gaps = []
        for p in points:
            if len(filled_gaps) > 0:
                while True:
                    last_p = filled_gaps[-1]
                    gap_size = Sequence.vector(last_p, p)
                    if not Sequence.fuzzyEqual(gap_size, delta):
                        # fill the gap
                        in_gap = (last_p[0] + delta[0], last_p[1] + delta[1])
                        filled_gaps.append(in_gap)
                    else:
                        break
            filled_gaps.append(p)

        return filled_gaps


if __name__ == '__main__':
    points = [(128, 470), (43, 390), (38, 380), (73, 346), (120, 342), (95, 236), (95, 236), (165, 338), (136, 232),
              (136, 232), (175, 228), (175, 228), (215, 224), (215, 224), (254, 220), (254, 220), (432, 296),
              (293, 216), (293, 216), (5, 196), (127, 101), (128, 101), (153, 95), (153, 95), (465, 87), (284, 84),
              (284, 84), (413, 73), (413, 73), (541, 62), (541, 62)]

#   points1 = [(0, 0), (20, 30), (30, 10), (60, 20), (80, 10), (90, 30)]

#   to_fill = [(0, 0), (0, 1), (0, 4), (0, 7)]

    seq = Sequence(points)
#   print(seq.marks)
#   p1 = Point(1, 2)
#   p2 = Point(6, -1)
#   print(p1, p2, p1 * 3)
#   print(p1, p2, p1-p2)
