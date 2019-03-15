# P4 Demo
This repo contains two highly simplified demo directories: mapreduce and threads_and_sockets

We hope that these demos provide a foundation for you to get started on Project 4. You will have to build on the concepts presented in this demo, the spec, and the lecture slides in order to build a fully functional MapReduce server like the one necessary for P4
<br><br>

## mapreduce
To run the finished job, use the following:
```bash
$ cat input/* | python wc_map.py | sort | python wc_reduce.py
```
You can also use the script `wc.sh`, which is simply the above bash command written in an executable script
```bash
$ ./wc.sh
```
You should see the following output when completed:
```shell
(targaryen?)	1
are	            1
arya	        1
best	        1
characters	    1
daenerys	    1
game	        1
jon	            1
lannister	    1
ned	            1
of	            1
snow	        1
stark	        2
targaryen	    1
the	            1
thrones	        1
tyrion	        1
```
<br>

## threads_and_sockets
To run this portion of the demo, open two terminal windows and navigate to the `threads_and_sockets` directory.
Then, create and activate a virtual environment.
```bash
$ python3 -m venv env
$ source env/bin/activate
```
Then, install the dependencies for the demo.
```bash
$ pip install -e .
```

From one window, run the following:
```bash
$ python listen.py
```
From the other window, run the following:
```bash
$ python send.py
```
There are lots of comments explaining the complicated socket code that you hopefully find helpful. Please reach out if you have any questions.
