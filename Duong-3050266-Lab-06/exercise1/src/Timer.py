import time

class Timer:
  def __init__(self):
    self.start_time = None
    self.end_time = None

  def start(self):
    if (self.start_time):
      raise ValueError("This timer instance has already started")
    self.start_time = time.process_time_ns()
    return self

  def end(self):
    if (self.end_time):
      raise ValueError("This timer instance has already ended")
    self.end_time = time.process_time_ns()
    return self

  def get_time(self):
    if (self.end_time and self.start_time):
      return self.end_time - self.start_time
    else:
      raise ValueError(f"This timer instance has not {'started' if not self.start_time else 'ended'}")

  def reset(self):
    self.start_time = None
    self.end_time = None
    return self
    