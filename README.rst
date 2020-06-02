*********
Berry forest
*********

|License|

- `About the project <README.rst#about-the-project>`_
- `Legal disclaimer <README.rst#legal-disclaimer>`_
- `Author <README.rst#author>`_
- `License <README.rst#license>`_

About the project
=================

This is a proof of concept on how to control a Raspberry pi from the browser.
Most of the pin numbers are hardcoded, adjust to match your setup.
The templates files are horribly hardcoded as well, especially the js part.


Build the container image
=================
::
 docker build -t berry_forest .
::

Build the container image
=================
::
docker container run -p 8080:8080 -d --privileged -d berry_forest
::

// TODO try this instead
::
docker container run --device /dev/gpiomem -d berry_forest 
::


::
docker update --restart=always 0576df221c0b
::

Legal disclaimer
=================
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Author
=======

Berry forest was created by `Michele Valsecchi <https://github.com/MicheleV>`_


License
=======

i2c_lib.py, lcddriver.py were provided natbett of the Raspberry Pi Forum, 2018 Feb 18th at [1]
Those two files are released under an unkown license, as the author has no contact information.

lcd.py is a derivative work based off from [2].

All the other files are released under GNU General Public License v3.0

See `COPYING <COPYING>`_ to see the full text.

[1] https://www.raspberrypi.org/forums/viewtopic.php?p=1314949&sid=385c6b728fc3ce85142749e13967cc54

[2] https://github.com/the-raspberry-pi-guy/lcd

.. |License| image:: https://img.shields.io/badge/license-GPL%20v3.0-brightgreen.svg
   :target: COPYING
      :alt: Repository License
