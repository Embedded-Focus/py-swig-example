#include <example.h>

#include <stdlib.h>

struct Handler_ {
  int value;
};

Handler alloc_something(void) {
  Handler result = malloc(sizeof(Handler));
  result->value = 23;
  return result;
}

void set_something(Handler handler, int value) {
  handler->value = value;
}

int get_something(Handler handler) {
  return handler->value;
}

void free_something(Handler handler) {
  free(handler);
}
