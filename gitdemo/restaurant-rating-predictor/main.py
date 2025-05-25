import os

def run_task(task_file):
    print(f"\n--- Running {task_file} ---")
    os.system(f"python {task_file}")

def main():
    while True:
        print("\nSelect a task to run:")
        print("1. Preprocess Data")
        print("2. Predict Restaurant Ratings (Task 1)")
        print("3. Restaurant Recommendation (Task 2)")
        print("4. Cuisine Classification (Task 3)")
        print("5. Geographical Analysis (Task 4)")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            run_task('preprocess.py')
        elif choice == '2':
            run_task('task1_predict_rating.py')
        elif choice == '3':
            run_task('task2_recommendation.py')
        elif choice == '4':
            run_task('task3_cuisine_classification.py')
        elif choice == '5':
            run_task('task4_geographical_analysis.py')
        elif choice == '0':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
