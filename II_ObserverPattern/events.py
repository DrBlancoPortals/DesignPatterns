from typing import Callable
#from dataclasses import field

#subscribers:dict = field(default_factory=dict)
subscribers = dict()

def subscribe(event_type: str,function:Callable):
    """Function in charge of adding subscribers to the event

    Args:
        event_type (str): key for the event
        function (Callable): function called uppon being notified
    """
    if not event_type in subscribers:
        # This is done to avoid the overwriting of existing 
        # subscribers
        subscribers[event_type] = []
    subscribers[event_type].append(function)

# This event system, as it is right now, would allow several 
# functions to be called for a given event identifier (str). 
# In a way, this would make it difficult to remove events.


def unsubscribe(event_type: str):
    """Function to unsubscribe events from the system

    Args:
        event_type (str): key to identify the events to be removed
    """
    try:
        subscribers.pop(event_type)
    except KeyError as e:
        print(e)


def post_event(event_type:str,data):
    """Function that posts events for the subscribed objects

    Args:
        event_type (str): key for the event
        data (_type_): Data passed to the funcions stored under each key
    """     
    if not event_type in subscribers:
        # In case of not having the event_type provided 
        # in the list of events (dictionay ... whatever)
        return
    for fn in subscribers[event_type]:
        fn(data)
    
# Notice that this would be doing the job of the subject. It bassically can subscribe observers (add) 
# and posts events to them, in case that the state has changed.