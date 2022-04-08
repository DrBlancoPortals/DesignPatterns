from dataclasses import field

#subscribers:dict = field(default_factory=dict)
subscribers = dict()

def subscribe(self,event_type: str,function):
    if not event_type in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(function)

def post_event(self,event_type:str,data):
    if not event_type in subscribers:
        return
    for fn in subscribers[event_type]:
        fn(data)
    
# Notice that this would be doing the job of the subject. It bassically can subscribe observers (add) 
# and posts events to them, in case that the state has changed.