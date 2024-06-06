# Transfer Functions in Python

Modeling the real world is hard. Physics often gives us differential equations, which are not so easy to solve, so what do we do? One option is to use a transfer function, which simplifies the differential equation into an algebraic one. Great. So now that we have something simpler, we can test different system inputs and measure the output in a simpler manner - no forward euler step simulations needed. 

starting with different differential equations yields different transfer functions, the following script shows the step input (which sets the input to the differential equation to 1 at time zero) to the three simplest and most widely used transfer functions. 