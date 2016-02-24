class BitQueryLookupWrapper(object):
    def __init__(self, alias, column, bit):
        self.table_alias = alias
        self.column = column
        self.bit = bit

    def as_sql(self, qn, connection=None):
        """
        Create the proper SQL fragment. This inserts something like
        "(T0.flags & value) != 0".

        This will be called by Where.as_sql()
        """
        query = '%s.%s | %d' if self.bit else '%s.%s & %d' 

        return query % (qn(self.table_alias), qn(self.column), self.bit.mask), []


class BitQuerySaveWrapper(BitQueryLookupWrapper):
    def as_sql(self, qn, connection):
        """
        Create the proper SQL fragment. This inserts something like
        "(T0.flags & value) != 0".

        This will be called by Where.as_sql()
        """
        query = '%s.%s | %d' if self.bit else '%s.%s & ~%d' 

        return query % (qn(self.table_alias), qn(self.column), self.bit.mask), []
