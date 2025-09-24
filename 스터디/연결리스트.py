class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link
class LinkedList:                    #연결된 리스트 클래스
    def __init__(self):
        self.head = None
    def isEmpty(self): return self.head == None    #공백상태 검사
    def clear(self): self.head = None              #리스트 초기화
    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count
    def display(self, msg):
        print(msg, end='')
        node = self.head
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()
    def getNode(self, pos):                     #pos번째 노드 반환
        if pos < 0: return None
        node = self.head;                       #node는 head부터 시작
        while pos > 0 and node != None:         #pos번 반복
            node = node.link                    #node를 다음 노드로 이동
            pos -= 1                            #남은 반복 횟수 줄임
        return node                             #최종 노드 반환
    def getEntry(self, pos):                  #pos번째 노드의 데이터 반환
        node = self.getNode(pos)              #pos번째 노드
        if node == None : return None         #찾는 노드가 없는 경우
        else : return node.data               #그 노드의 데이터 필드 반환
    def replace(self, pos, elem):             #pos번째 노드의 데이터를 변경
        node = self.getNode(pos)              #pos번째 노드를 찾아
        if node != None: node.data = elem     #데이터 필드에 elem 복사
    def find(self, data):                           #데이터로 data를 갖는 노드 반환
        node = self.head;
        while node is not None:                     #모든 노드에서 찾음
            if node.data == data : return node      #찾아지면 바로 반환
            node = node.link
        return node                                 #찾아지지 않으면 None 반환
    def insert(self, pos, elem):
        before = self.getNode(pos-1)                #before 노드를 찾음
        if before == None:                          #맨 앞에 삽입하는 경우
            self.head = Node(elem, self.head)       #맨앞에 삽입함
        else:                                       #중간에 삽입하는 경우
            node = Node(elem, before.link)          #노드 생성 + Step1
            before.link = node                      #Step2
    def delete(self, pos):
        before = self.getNode(pos-1)                #before 노드를 찾음
        if before == None:                          #시작 노드를 삭제
            if self.head is not None:               #공백이 아니면
                self.head = self.head.link          #head를 다음으로 이동
        elif before.link != None:                   #중간에 있는 노드 삭제
            before.link = before.link.link          #Step1
s = LinkedList()
s.display('단순연결리스트로 구현한 리스트(초기상태):')
s.insert(0, 10);    s.insert(0, 20);     s.insert(1, 30)
s.insert(s.size(), 40); s.insert(2, 50)
s.display("단순연결리스트로 구현한 리스트(삽입x5): ")
s.replace(2, 90)
s.display("단순연결리스트로 구현한 리스트(교체x1): ")
s.delete(2);    s.delete(s.size() - 1); s.delete(0)
s.display("단순연결리스트로 구현한 리스트(삭제x3): ")
s.clear()
s.display("단순연결리스트로 구현한 리스트(정리후): ")

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self
        self.next = self
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self.head is None
    def append(self, data):
        """맨 뒤에 노드 추가"""
        new = Node(data)
        if self.is_empty():
            self.head = new
        else:
            tail = self.head.prev
            tail.next = new
            new.prev = tail
            new.next = self.head
            self.head.prev = new
        self._size += 1
    def prepend(self, data):
        """맨 앞에 노드 추가"""
        self.append(data)
        self.head = self.head.prev  # 방금 추가한 노드를 새 head로
    def find(self, predicate):
        """조건을 만족하는 첫 노드 반환 없으면 None"""
        if self.is_empty():
            return None
        cur = self.head
        for _ in range(self._size):
            if predicate(cur.data):
                return cur
            cur = cur.next
        return None
    def insert_after(self, node, data):
        """특정 노드 뒤에 삽입"""
        if node is None:
            return
        new = Node(data)
        nxt = node.next
        node.next = new
        new.prev = node
        new.next = nxt
        nxt.prev = new
        self._size += 1
    def remove_node(self, node):
        """특정 노드 제거"""
        if node is None or self.is_empty():
            return False
        if self._size == 1:
            self.head = None
            self._size = 0
            return True
        # 연결 재배치
        node.prev.next = node.next
        node.next.prev = node.prev
        # 제거 노드가 head이면 다음 노드를 head로
        if node is self.head:
            self.head = node.next
        self._size -= 1
        return True
    def remove(self, data):
        """값으로 제거 첫 일치만"""
        target = self.find(lambda x: x == data)
        return self.remove_node(target)
    def rotate(self, k=1, to_left=True):
        """원형 회전. to_left True면 왼쪽으로 k칸 이동"""
        if self.is_empty() or k % self._size == 0:
            return
        steps = k % self._size
        cur = self.head
        for _ in range(steps):
            cur = cur.next if to_left else cur.prev
        self.head = cur
    def to_list_forward(self):
        """head부터 시계 방향 리스트"""
        out = []
        if self.is_empty():
            return out
        cur = self.head
        for _ in range(self._size):
            out.append(cur.data)
            cur = cur.next
        return out
    def to_list_backward(self):
        """head의 이전부터 반시계 방향 리스트"""
        out = []
        if self.is_empty():
            return out
        cur = self.head.prev  # tail부터 역순
        for _ in range(self._size):
            out.append(cur.data)
            cur = cur.prev
        return out
    def __iter__(self):
        """for 순회 지원"""
        if self.is_empty():
            return
        cur = self.head
        for _ in range(self._size):
            yield cur.data
            cur = cur.next
    def debug_print(self, limit=16):
        """원형 구조 확인용 간단 출력"""
        if self.is_empty():
            print("[]")
            return
        cur = self.head
        out = []
        for _ in range(min(self._size, limit)):
            out.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(out))
# 사용 예시
if __name__ == "__main__":
    fruits = ["사과", "배", "포도", "바나나", "복숭아", "자두", "키위", "파인애플"]
    cdll = CircularDoublyLinkedList()
    for f in fruits:
        cdll.append(f)
    print("초기 상태 시계 방향:", cdll.to_list_forward())
    print("초기 상태 역방향:", cdll.to_list_backward())
    print("크기:", len(cdll))
    # 특정 원소 뒤에 삽입
    node = cdll.find(lambda x: x == "바나나")
    cdll.insert_after(node, "망고")
    print("바나나 뒤에 망고 삽입:", cdll.to_list_forward(), "크기:", len(cdll))
    # 원소 제거
    cdll.remove("포도")
    print("포도 제거 후:", cdll.to_list_forward(), "크기:", len(cdll))
    # 회전
    cdll.rotate(k=3, to_left=True)
    print("왼쪽으로 3칸 회전:", cdll.to_list_forward(), "현재 head:", cdll.head.data)
    cdll.rotate(k=2, to_left=False)
    print("오른쪽으로 2칸 회전:", cdll.to_list_forward(), "현재 head:", cdll.head.data)
    # 앞뒤 추가
    cdll.prepend("체리")
    print("앞에 체리 추가:", cdll.to_list_forward(), "현재 head:", cdll.head.data)
    cdll.append("레몬")
    print("뒤에 레몬 추가:", cdll.to_list_forward(), "크기:", len(cdll))
    # 디버그 출력
    print("최종 결과: ")
    cdll.debug_print()