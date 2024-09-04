class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # arrange cars in order of closest to finish first
        # iterate through checking if next closest catches up
        # CatchUp formula = remaining steps / speed to next car
        # if it doesnt then add curr car finish time to stack
        stack = []
        cars = []
        for i in range(len(speed)) :
            cars.append([position[i], speed[i]])
        cars = sorted(cars, reverse=True)

        for i, car in enumerate(cars):
            time_to_target = (target - car[0]) / car[1]
            if stack and stack[-1] >= time_to_target:
                pass
            else:
                stack.append(time_to_target)
        return len(stack)

