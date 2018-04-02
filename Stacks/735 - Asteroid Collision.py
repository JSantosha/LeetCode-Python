class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        collisions = []
        for i in xrange(len(asteroids)):
            t = len(collisions) - 1
            if len(collisions) != 0:
                if collisions[t] > 0 and asteroids[i] < 0:
                    if abs(collisions[t]) == abs(asteroids[i]):
                        collisions.pop()
                        t = len(collisions) - 1
                        continue
                    while abs(collisions[t]) < abs(asteroids[i]):
                        collisions.pop()
                        t = len(collisions) - 1
                        if t < 0 or collisions[t] < 0 or abs(collisions[t]) == abs(asteroids[i]):
                            break
                    if t < 0 or collisions[t] < 0 and asteroids[i] < 0:
                        collisions.append(asteroids[i])
                        t = len(collisions) - 1
                    elif collisions[t] > 0 and asteroids[i] < 0 and abs(collisions[t]) == abs(asteroids[i]):
                        collisions.pop()

                else:

                    collisions.append(asteroids[i])
                    t = len(collisions) - 1
            else:
                collisions.append(asteroids[i])
                t = len(collisions) - 1

        return collisions
