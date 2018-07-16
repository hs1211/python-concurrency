Concurrency
===========

파이썬에서 동시성 처리를 고려할 경우 많이 듣게 되는 것이 바로 GIL이다. GIL을 사용할 경우에 우리가 원하는 만큼의 성능이 나오지 않을 수 있다.
그래서 대안으로 Cython을 통하여 약 100배에 달하는 성능향상을 가져올 수 도 있다.

::

    파이썬의 인터프린트는 한갱의 코어 프로세스에서만 동작한다 이때 락을 GIL(Global Interpreter Lock)이라고 한다.
    그렇지 않다면 멀티 프로세스 개념을 통하여 GIL을 회피하는 것도 한가지 대안이 될 수 있다.


3 Level Concurrency
-------------------

::

    먼저 태스크를 종류에 따라 구분한다면 크게 2가지로 CPU bound 업무와 I/O bound 업무로 구분가능하다.
    CPU bound 태스크의 경우에는 멀티 프로세스를 도입하여 GIL을 회피하는 것도 한가지 대안이 될 수 있다.
    그리고 I/O bound 태스크에는 멀티 스레드나 멀티 태스크 보다는 network latency와 같은 것이 주요한 원인이 될 수 있다.


여기서는 Concurrency를 세 단계로 나누어서 살펴보기로 하자.

    1. Low-Level Concurrency

        해당 레벨의 동시성은 원자성 연산(atomic operation)을 명시적으로 사용하는 것을 의미하며 어플리케이션 작성자보다는 라이브러리 개발자가 많이 사용한다
        이 레벨의 동시성은 파이썬에서 제공하지 않는다

    2. Mid-Level Concurrency

        이 레벨에 해당하는 동시성은 원자성 연산을 사용하지느 않지만 락을 사용한 동시성 제어가 이루어지는 것을 의미한다. 대부분은의 언어가 지원하고 있으며 파이썬에서는 다음와 같은 클래스가 이에 해당한다.
        e.g) threading.Semaphore, threading.Lock, multiprocessing.Lock

    3. High-Level Concurrency

        원자성 연산이나 락을 사용하는 것이 아닌 동시성을 의미하며 파이썬에서는 concurrent.futures나 queue모듈등이 이에 해당한다.


위에서 언급한 것과 같이 다양한 레벨로 동시성 제어가 가능하다. 하지만 Mid-Level로 동시성을 제어할 경우에 에러(error prone)가 발생할 가능성이 높아진다. 핵심 이슈는 데이터 공유에 있다
그러므로 가능하다면 짧은 시간만 락을 걸어서 사용해야 한다. 더 좋은 방법은 데이터 공유를 안하는 것이다. 공유하지 않는다면 락에 대한 문제는 사라지게 된다.

이런 예로 큐를 사용하는 것이 있는데 multiprocessing.JoinableQueue and multiprocessing.Queue가 해당된다. 이들 자료구조가 동시성 문제를 지원하는 자료구조들이다.

Example
-------

| 여기에서는 두가지 예제를 다룰 예정이다. 둘다 High-Level Concurrency를 활용하고 있으며 하나는 CPU-bound 태스크를 또 다른 하나는 I/O-bound 태스크에 해당한다.
| 각각의 링크는 아래와 같다


+-------------------------------+
|           SUMMARY             |
+-------------------------------+
|     `CPU Bound Concurrency`_  |
+-------------------------------+
|     `I/O Bound Concurrency`_  |
+-------------------------------+


.. _`CPU Bound Concurrency`: ./cpu-bound-concurrency/README.rst
.. _`I/O Bound Concurrency`: ./io-bound-concurrency/README.rst



