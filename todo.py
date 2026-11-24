"""A small command-line task tracker backed by a JSON file."""

from storage import TaskStorage


class TodoApp:
    def __init__(self, storage=None):
        self.storage = storage or TaskStorage()

    def run(self):
        print("할 일 목록에 오신 것을 환영합니다!")
        while True:
            print("\n1) 목록  2) 추가  3) 완료 표시  4) 삭제  5) 종료")
            choice = input("> ").strip()
            if choice == "1":
                self.show_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("종료합니다.")
                break
            else:
                print("1부터 5 사이의 메뉴를 선택해 주세요.")

    def show_tasks(self):
        tasks = self.storage.load()
        if not tasks:
            print("등록된 할 일이 없습니다.")
            return
        for task in tasks:
            mark = "✓" if task["done"] else " "
            print(f'{task["id"]}. [{mark}] {task["title"]}')

    def add_task(self):
        title = input("할 일: ").strip()
        if not title:
            print("빈 내용은 추가할 수 없습니다.")
            return
        tasks = self.storage.load()
        next_id = max((task["id"] for task in tasks), default=0) + 1
        tasks.append({"id": next_id, "title": title, "done": False})
        self.storage.save(tasks)
        print("추가했습니다.")

    def complete_task(self):
        self._update_task("완료 표시", lambda task: task.update(done=True))

    def delete_task(self):
        try:
            task_id = int(input("삭제할 번호: "))
        except ValueError:
            print("번호를 입력해 주세요.")
            return
        tasks = self.storage.load()
        remaining = [task for task in tasks if task["id"] != task_id]
        if len(remaining) == len(tasks):
            print("해당 번호를 찾을 수 없습니다.")
            return
        self.storage.save(remaining)
        print("삭제했습니다.")

    def _update_task(self, message, update):
        try:
            task_id = int(input("대상 번호: "))
        except ValueError:
            print("번호를 입력해 주세요.")
            return
        tasks = self.storage.load()
        task = next((item for item in tasks if item["id"] == task_id), None)
        if task is None:
            print("해당 번호를 찾을 수 없습니다.")
            return
        update(task)
        self.storage.save(tasks)
        print(f"{message}했습니다.")
