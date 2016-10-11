# WAITLIST EXCHANGE

## What?

Many times, in places like college or with vacations or various other parts of life, we come to a point where we would like to trade with others. More specifically, we want to be part of a trading circle: person A gives something person B, person B to person C, ..., person K to person A.

Unfortunately, we can't talk to everybody and don't know of people who have whatever we'd like. Or, maybe, we don't know if we can trade with multiple people to form longer trading chains.

So, we decided to make a simple website to let people do this.

## How?

This is all done in the python standard library on the server-side and HTML and jQuery on the client end and JSON for all the necessary communication and databasing (though a CSV database may be used later on).

The internals of the server involve a graph algorithm to find all the cycles. These cycles are possible trades.

## What now?

We are trying to get this to universities and/or any other interested companies soon.

## This Repo.

This repository has a simple structure:
- The web folder has all the client-facing code organized by language.
- The db folder has all the data.
- Classes.py and subsets.py form the backend. 
- srv\_util.py acts as a layer between the server and the backend and database. 
- srv.py implements and runs the server.

## Where are we?

So far we have a working demo. That's about it...

We have yet to test and offer this to companies.
