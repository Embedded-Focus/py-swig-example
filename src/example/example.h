#ifndef EXAMPLE_H
#define EXAMPLE_H

typedef struct Handler_ Handler_;
typedef Handler_ *Handler;
extern Handler alloc_something(void);
extern void set_something(Handler handler, int value);
extern int get_something(Handler handler);
extern void free_something(Handler handler);

#endif /* EXAMPLE_H */
