# proxyscan

proxyscan essentially performs a portscan via an HTTP proxy

# Examples / Usage

```
> cat interesting_hosts 
66.228.43.44
74.207.249.32
adhara:/me/home/devel/proxyscan>> cat in
interesting_hosts  interesting_ports  
> cat interesting_ports 
80
#blah
22
> cat proxies 
127.0.0.1 3128
```

```
python proxyscan.py
          127.0.0.1  3128     66.228.43.44  80    403
          127.0.0.1  3128     66.228.43.44  22    403
          127.0.0.1  3128    74.207.249.32  80    403
          127.0.0.1  3128    74.207.249.32  22    403
--- successful connection summary ---
```

# Copyright and License

Copyright (C) 2016 Steve Benson

proxyscan was written by Steve Benson.

proxyscan is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation; either version 3, or (at your option) any later
version.

proxyscan is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
this program; see the file LICENSE.  If not, see <http://www.gnu.org/licenses/>.
