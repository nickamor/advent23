#include <stdio.h>
#include <stdlib.h>
#include <regex.h>

const char *filename = "./day05/test";

char *read_file(const char *filename)
{
    FILE *fp = fopen(filename, "r");
    fseek(fp, 0, SEEK_END);

    size_t size = ftell(fp);
    char *buffer = (char *)malloc(sizeof(char) * size + 1);
    rewind(fp);

    fread(buffer, sizeof(char), size, fp);
    buffer[size] = '\0';

    fclose(fp);
    return buffer;
}

typedef struct list_t
{
    void *data;
    struct list_t *next;
} LIST;

typedef void (*LIST_ITEM_FN)(void *);

typedef struct seed_t
{
    int source;
    int len;
} SEED;

typedef struct map_t
{
    // MAP_NODE**
    LIST *nodes;
} MAP;

typedef struct map_node_t
{
    int dest;
    int source;
    int len;
} MAP_NODE;

typedef struct input_t
{
    // SEED**
    LIST *seeds;
    // MAP**
    LIST *maps;
} INPUT;

SEED *create_seed(int source, int len)
{
    SEED *seed = malloc(sizeof(SEED));
    seed->source = source;
    seed->len = len;
    return seed;
}

MAP_NODE *create_node(int dest, int source, int len)
{
    MAP_NODE *node = malloc(sizeof(MAP_NODE));
    node->dest = dest;
    node->source = source;
    node->len = len;
    return node;
}

MAP *create_map(LIST *nodes)
{
    MAP *map = malloc(sizeof(MAP));
    map->nodes = nodes;
    return map;
}

LIST *create_list(void *data)
{
    LIST *list = malloc(sizeof(LIST));
    list->data = data;
    list->next = NULL;
    return list;
}

LIST *list_tail(LIST *list)
{
    LIST *tail = list;
    while (tail->next != NULL)
    {
        tail = tail->next;
    }
    return tail;
}

void list_push(LIST **list, void *data)
{
    if (*list == NULL)
    {
        *list = create_list(data);
        return;
    }

    LIST *tail = list_tail(*list);

    tail->next = create_list(data);
}

SEED *parse_seeds(const char *input)
{
    SEED *data = malloc(sizeof(SEED));

    regex_t regex;
    regcomp(&regex, "seeds: (.*)\n", REG_EXTENDED | REG_NEWLINE);
    regmatch_t pmatch[2];

    const char *str = input;
    int count = 0;
    while (regexec(&regex, str, 2, pmatch, 0) == 0)
    {
        count++;
        const char *match_start = str + pmatch[1].rm_so;
        const char *match_end = str + pmatch[1].rm_eo;

        int s = (match_end - match_start) + 1;
        char match[s];
        for (int i = 0; i < s; i++)
        {
            match[i] = match_start[i];
        }
        match[s] = '\0';

        printf("match:: %s\n", match);
        // printf("Found: %d\n", atol(match));

        str = match_end;
    }
    printf("matched %d times\n", count);

    // regfree(&regex);

    return data;
}

MAP *parse_maps(const char *input)
{
    MAP *map = create_map(NULL);

    map->nodes = create_list(NULL);

    MAP_NODE *n1 = create_node(1, 2, 3);
    MAP_NODE *n2 = create_node(4, 5, 6);

    list_push(&map->nodes, n1);
    list_push(&map->nodes, n2);

    return map;
}

INPUT *parse_input(const char *input)
{
    INPUT *data = malloc(sizeof(INPUT));

    list_push(&data->seeds, parse_seeds(input));
    list_push(&data->maps, parse_maps(input));

    return data;
}

void for_each(LIST *head, LIST_ITEM_FN fn)
{
    LIST *current = head;
    while (current != NULL)
    {
        fn(current->data);
        current = current->next;
    }
}

void debug_seed(SEED *seed)
{
    printf("  seed %d %d\n", seed->source, seed->len);
}

void debug_map_node(MAP_NODE *node)
{
    printf("  node %d %d %d\n", node->dest, node->source, node->len);
}

void debug_map(MAP *map)
{
    printf(" map:\n");
    for_each(map->nodes, debug_map_node);
}

void debug_input(INPUT *input)
{
    printf("seeds:\n");
    for_each(input->seeds, debug_seed);

    printf("\n");

    printf("maps:\n");
    for_each(input->maps, debug_map);
}

int main(int argc, char **argv)
{
    char *lines = read_file(filename);
    INPUT *input = parse_input(lines);

    debug_input(input);

    return EXIT_SUCCESS;
}
