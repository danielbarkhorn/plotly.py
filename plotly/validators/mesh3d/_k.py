import _plotly_utils.basevalidators


class KValidator(_plotly_utils.basevalidators.DataArrayValidator):

    def __init__(self, plotly_name='k', parent_name='mesh3d', **kwargs):
        super(KValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='data',
            **kwargs
        )