{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNuaUqV5ND+iCjmd4vWKRpw",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/faeyra/faeyra/blob/main/test.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pEdJ0XLd8Afc",
        "outputId": "c7d9e600-812e-464c-954c-93853c5402b3"
      },
      "source": [
        "greeting='hello world'\n",
        "\n",
        "for i in greeting:\n",
        "  print(i)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "h\n",
            "e\n",
            "l\n",
            "l\n",
            "o\n",
            " \n",
            "w\n",
            "o\n",
            "r\n",
            "l\n",
            "d\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kCw0IL7b99s6"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "i-BCPj65_MaJ"
      },
      "source": [
        "from tensorflow.python.client import device_lib "
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HhxaWM-lAL9b",
        "outputId": "50d6f2e4-1e5b-49e3-985a-cbd9ecd3411c"
      },
      "source": [
        "!cat /proc/meminfo"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "MemTotal:       13305368 kB\n",
            "MemFree:         9446280 kB\n",
            "MemAvailable:   12057476 kB\n",
            "Buffers:           86368 kB\n",
            "Cached:          2516240 kB\n",
            "SwapCached:            0 kB\n",
            "Active:          1272044 kB\n",
            "Inactive:        2197056 kB\n",
            "Active(anon):     676660 kB\n",
            "Inactive(anon):    10672 kB\n",
            "Active(file):     595384 kB\n",
            "Inactive(file):  2186384 kB\n",
            "Unevictable:           0 kB\n",
            "Mlocked:               0 kB\n",
            "SwapTotal:             0 kB\n",
            "SwapFree:              0 kB\n",
            "Dirty:               396 kB\n",
            "Writeback:             0 kB\n",
            "AnonPages:        866428 kB\n",
            "Mapped:           604272 kB\n",
            "Shmem:             11408 kB\n",
            "KReclaimable:     141808 kB\n",
            "Slab:             200184 kB\n",
            "SReclaimable:     141808 kB\n",
            "SUnreclaim:        58376 kB\n",
            "KernelStack:        5088 kB\n",
            "PageTables:         8540 kB\n",
            "NFS_Unstable:          0 kB\n",
            "Bounce:                0 kB\n",
            "WritebackTmp:          0 kB\n",
            "CommitLimit:     6652684 kB\n",
            "Committed_AS:    3892224 kB\n",
            "VmallocTotal:   34359738367 kB\n",
            "VmallocUsed:       51244 kB\n",
            "VmallocChunk:          0 kB\n",
            "Percpu:             1400 kB\n",
            "AnonHugePages:         0 kB\n",
            "ShmemHugePages:        0 kB\n",
            "ShmemPmdMapped:        0 kB\n",
            "FileHugePages:         0 kB\n",
            "FilePmdMapped:         0 kB\n",
            "CmaTotal:              0 kB\n",
            "CmaFree:               0 kB\n",
            "HugePages_Total:       0\n",
            "HugePages_Free:        0\n",
            "HugePages_Rsvd:        0\n",
            "HugePages_Surp:        0\n",
            "Hugepagesize:       2048 kB\n",
            "Hugetlb:               0 kB\n",
            "DirectMap4k:      214216 kB\n",
            "DirectMap2M:     6076416 kB\n",
            "DirectMap1G:     9437184 kB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MmRY0NDaA0Bn",
        "outputId": "18b01611-4eb6-4b34-8671-e683a53e2c7b"
      },
      "source": [
        "%history\n",
        "\n"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "from tensorflow.python.client import device_lib\n",
            "device _lib.list_local_devices()\n",
            "from tensorflow.python.client import device_lib\n",
            "device\n",
            "from tensorflow.python.client import device_lib device_lib.list_local_devices\n",
            "from tensorflow.python.client import device_lib device_lib.list_local_devices()\n",
            "from tensorflow.python.client import device_lib\n",
            "device_lib.list_local_devices()\n",
            "!cat /proc/meminfo\n",
            "%history\n",
            "%history\n",
            "%Idir\n",
            "%history\n",
            "% Idir\n",
            "%history\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "75J-Y_GXA-OO"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}