Test
=========

.. graph:: images/g.png
    :scale: 50%

       digraph g {
                rankdir="LR"

                edge [fontcolor=red fontsize=9]
                node [shape=box style="rounded"]

                wmsc [label="WMS-client"]
                wmsc2 [label="WMS-client"]
                wmss [label="WMS-server" shape=box style=""]

                wmsc -> wmss [label="KVP request"]
                wmss -> wmsc2 [label="image response"]

        }



