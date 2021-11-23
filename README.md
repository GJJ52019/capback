# SimPy Storage
  The object with this repo is to demonstrate a possible setup for a django database to host data from a simpy file


##  current state
Currently the database is deployed and hosted but there is no link between it and the simulation file.

## Technologies Used:

- SimPy
- JavaScript
- JSON
- Python
- Django
- Heroku

## links:
- https://trello.com/b/5iGVBVaq/capstone
- https://simpy-storage.herokuapp.com/

## Screenshots:

- idea for how the data should be stored once in json
![image](https://i.imgur.com/l5JFkEu.jpg)

- final erd for simulation
![image](https://i.imgur.com/rNycnCk.png)

- flow chart for simulation
![image](https://i.imgur.com/8fWoESF.jpg)

-Simulation run 
![image](https://i.imgur.com/4fq2NRx.png)


## Getting Started:
- currently the data is full CRUD but no way to automate the postings.
- The current model while a place holder is an insight into the complex amount of variables that go into making a simulation and the data it can hold.
- user can edit the data to create a log for them selves to work with if they wanted to to keep track of metrics across the day.
- the simulation file is not yet included due to breaking the heroku the first time it was
- once a simpy file is made it still must be run with the terminal using (py/python/python3 filename)
- 


## Future Enhancements:
- Simpy file to post to database.
- change the model from days to hours for better tracking.
- if possible make a way to trigger simulation file from online site.


--------------------------------------------------------------------------

# SimPY markdown

# Contents
- Explanation of Simpy
- Breakdown of a what a simulation is with simPY
- Yield vs return
- Thoughts on global variable
- monitoring

## What is SimPY

Simpy is a python module that allows the use of environmnets to run basic simulation of our creation to run and be modeled after real life examples. These are DES models or discrete event simulation. This means the events have a specific point in time during the event in which each event occurs.

### Link to documentation
- https://simpy.readthedocs.io/en/latest/index.html


## What comprises a simulation in SimPY

- Entities or Resources = the objects going through the simulation in this case the raw materials

- Generators = How the entities are brought into the simulation such as arrival at the plant from a stock delivery

- Arrival times = the time between stock deliveries if needed.

- Activity/process = the process happening to the entity

- Activity Time = the time it takes to go through the current process

- Resources = Whats neede to run the activity

- Queues/containers = holding pools for entities before they enter an activity

- Sinks = The exit point for the entity after all actvities

## Yield vs Return

Using generator functions instead of regular python fuctions is key to the simulator. Yield allows the function to be called numerous times from where it left off the last time is was called. Where as return will cause the funtion to reset when called again destroying previous results

## Using a global keyword

 I don't think this is best practice but until I understand simPY and python better I am forced to store the data generated in a global variable using the global keyword.

## Monitoring
This is the elusive key along with various other technologies needed in theory to get the simualtion to post to the database. Simpy includes a few ways to monitor the simulation as it goes along however they invlove the use of "args" and "Kwargs" from functools import partial, wraps. This end up being outside of the scope of current capabilities but will come back to it.

other technologies listed were the idea to use a combination of NumPy and Pandas to store the data than implement it. Another method was going to invlove usingpython to make a population script. However each of these methods also involved running the script from the terminal.
