class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude: int = 0
        curr_altitude: int = 0

        for i in range(len(gain)):
            curr_altitude += gain[i]
            print(curr_altitude)
            if highest_altitude < curr_altitude:
                highest_altitude = curr_altitude

        return highest_altitude