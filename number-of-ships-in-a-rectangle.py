class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        res = 0
        x, y = bottomLeft.x, bottomLeft.y
        while x <= topRight.x and y <= topRight.y:
            found = False
            beg = x
            end = topRight.x
            newx = topRight.x + 1
            while beg <= end:
                mid = (beg + end) // 2
                if sea.hasShips(Point(mid, topRight.y), Point(x, bottomLeft.y)):
                    found = True
                    newx = mid + 1
                    end = mid - 1
                else:
                    beg = mid + 1
            beg = y
            end = topRight.y
            newy = topRight.y + 1
            while beg <= end:
                mid = (beg + end) // 2
                if sea.hasShips(Point(topRight.x, mid), Point(bottomLeft.x, y)):
                    found = True
                    newy = mid + 1
                    end = mid - 1
                else:
                    beg = mid + 1
            if found:
                res += 1
            x = newx
            y = newy
        return res