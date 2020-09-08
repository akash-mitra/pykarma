signals = {
    's1': {
        "Comp A": "B",
        "Comp B": "B",
        "Comp C": "S",
        "Comp E": "H",
    },

    's2': {
        "Comp A": "H",
        "Comp B": "B",
        "Comp D": "B",
    },

    's3': {
        "Comp A": "S",
        "Comp B": "B",
        "Comp C": "S",
        "Comp D": "H",
    }
}

# if the priority order is fixed, the
# easiest way to merging will be this.
fixed_order_merge = {**signals['s1'], **signals['s2'], **signals['s3']}


# if the priorities are variable, stored
# in another tuple or list...
priority_order = ('s1', 's2', 's3')

variable_order_merge = {}
for source in priority_order:
    variable_order_merge.update(signals[source])


print(fixed_order_merge)
print(variable_order_merge)