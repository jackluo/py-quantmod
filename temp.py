def get_annotations(annotation):
    """
    Return a list with annotations.

    Parameters
    ----------
        annotation : dict
            Dict of annotations, but not all arguments need
            to be filled.

    Example
    -------
    get_annotation({'title' : text})

    """
    annotations = []
    if 'title' in annotations:
        annotations.append(
            dict(
                text=annotations['title'],
                showarrow=False,
                x=0,
                y=1,
                xref='paper',
                yref='paper',
            )
        )
    else:
        for key, value in annotation:
            maxv = df.ix[k].sum() if key in df.index else 0
            annotations.append(
                dict(
                    x=k,
                    y=maxv,
                    xref='x',
                    yref='y',
                    text=value,
                    showarrow=True,
                    arrowhead=7,
                    ax=0,
                    ay=-100,
                    textangle=-90
                )
            )

    return annotations


















	if any(k in kwargs for k in ['vline','hline','shapes','hspan','vspan']):
		shapes=[]

		def get_shapes(xline):
			orientation=xline[0]
			xline=kwargs[xline]
			if isinstance(xline,list):
				for x_i in xline:
					if isinstance(x_i,dict):
						x_i['kind']='line'
						shapes.append(get_shape(**x_i))
					else:
						if orientation=='h':
							shapes.append(get_shape(kind='line',y=x_i))
						else:
							shapes.append(get_shape(kind='line',x=x_i))
			elif isinstance(xline,dict):
				shapes.append(get_shape(**xline))
			else:
				if orientation=='h':
					shapes.append(get_shape(kind='line',y=xline))
				else:
					shapes.append(get_shape(kind='line',x=xline))

		def get_span(xspan):
			orientation=xspan[0]
			xspan=kwargs[xspan]
			if isinstance(xspan,list):
				for x_i in xspan:
					if isinstance(x_i,dict):
						x_i['kind']='rect'
						shapes.append(get_shape(**x_i))
					else:
						v0,v1=x_i
						if orientation=='h':
							shapes.append(get_shape(kind='rect',y0=v0,y1=v1,fill=True,opacity=.5))
						else:
							shapes.append(get_shape(kind='rect',x0=v0,x1=v1,fill=True,opacity=.5))
			elif isinstance(xspan,dict):
				xspan['kind']='rect'
				shapes.append(get_shape(**xspan))
			elif isinstance(xspan,tuple):
				v0,v1=xspan
				if orientation=='h':
					shapes.append(get_shape(kind='rect',y0=v0,y1=v1,fill=True,opacity=.5))
				else:
					shapes.append(get_shape(kind='rect',x0=v0,x1=v1,fill=True,opacity=.5))
			else:
				raise Exception('Invalid value for {0}span: {1}'.format(orientation,xspan))

		if 'hline' in kwargs:
			get_shapes('hline')
		if 'vline' in kwargs:
			get_shapes('vline')
		if 'hspan' in kwargs:
			get_span('hspan')
		if 'vspan' in kwargs:
			get_span('vspan')
		if 'shapes' in kwargs:
			shapes_=kwargs['shapes']
			if isinstance(shapes_,list):
				for i in shapes_:
					shp=i if 'type' in i else get_shape(**i)
					shapes.append(shp)
			elif isinstance(shapes_,dict):
					shp=shapes_ if 'type' in shapes_ else get_shape(**shapes_)
					shapes.append(shp)
			else:
				raise Exception("Shapes need to be either a dict or list of dicts")


		layout['shapes']=shapes


        # Check for argument integrity
        if title:
            if not isinstance(title, six.string_types):
                raise Exception("Invalid title '{0}'.".format(title))
        else:
            if self.ticker:
                title = ticker
            else:
                title = 'EQUITY'

        if self.start and self.end:
            if isinstance(self.start, str) and isinstance(self.end, str):
                title = title + ' [{0}/{1}]'.format(self.start, self.end)
