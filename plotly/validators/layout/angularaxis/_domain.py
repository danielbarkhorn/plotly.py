import _plotly_utils.basevalidators


class DomainValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self, plotly_name='domain', parent_name='layout.angularaxis', **kwargs
    ):
        super(DomainValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            items=[
                {
                    'editType': 'plot',
                    'max': 1,
                    'min': 0,
                    'valType': 'number'
                }, {
                    'editType': 'plot',
                    'max': 1,
                    'min': 0,
                    'valType': 'number'
                }
            ],
            role='info',
            **kwargs
        )