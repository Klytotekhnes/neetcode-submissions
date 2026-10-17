class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #TODO: sort position and speed, descend = True (for position)
        zipped_data = list(zip(position, speed))
        zipped_data.sort(key=lambda x: x[0], reverse=True)
        
        times_for_target = [(target - pos) / spd for pos, spd in zipped_data]
        res = 1
        current_time = times_for_target[0]
        for time in times_for_target[1:]:
            if time > current_time:
                res += 1
                current_time = time
                
        return res
            