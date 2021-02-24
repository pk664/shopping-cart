# shopping-cart

A Python application that allows users to identify their selected grocery items by the items ID. This application adds up product prices, calculates tax, and calculates the total amount due for the grocery items as well as prints out a receipt. 


# Prerequisites 
  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation


Fork this [remote repository](http://github.com/pk664/shopping-cart) under your own control, then "clone" or download your remote copy onto your local computer.


After cloning the repo, navigate there from the command-line:

```sh
cd shopping-cart
```

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env":

```sh
conda create -n shopping-env python=3.8
conda activate shopping-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Tax Rate Setup 

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired tax rate according to your state's tax rate. For example: 

    TAX_RATE="0.0875"

If no tax rate is specified by the user, then the default tax rate used in the application would be 8.75%. However, if a tax rate is specified by the user, then the tax rate used in the calculation would be the rate specified by the user. 


## Usage 

Run the program: 
```sh
python shopping_cart.py
```


