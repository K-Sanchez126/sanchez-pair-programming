{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6d1350ae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(np.float64(3.061616997868383e-16), np.float64(5.0))\n"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    "\n",
    "#Function that takes r and theta as input and outputs the x and y cooridnates \n",
    "def polar_to_cartesian(r, theta):\n",
    "    x= r * np.cos(theta)\n",
    "    y = r* np.sin(theta)\n",
    "    return x,y\n",
    "\n",
    "r= 5 \n",
    "theta = np.pi/2\n",
    "\n",
    "print(polar_to_cartesian(r, theta))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a81ac4f8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "GPGN268",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
