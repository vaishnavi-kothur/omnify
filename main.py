class Workout:
    def __init__(self, exercise, sets, reps):
        self.exercise = exercise
        self.sets = sets
        self.reps = reps

class WorkoutLog:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def delete_workout(self, index):
        del self.workouts[index]

    def edit_workout(self, index, workout):
        self.workouts[index] = workout

    def get_workouts(self):
        return self.workouts

# Sample usage
workout_log = WorkoutLog()
workout = Workout("Bench Press", 3, 10)
workout_log.add_workout(workout)
workout_log.delete_workout(0)
workout = Workout("Squats", 4, 12)
workout_log.edit_workout(0, workout)
workouts = workout_log.get_workouts()
for workout in workouts:
    print(workout.exercise, workout.sets, workout.reps)
