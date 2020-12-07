def ludwig_get_model_definition(df: 'Dataframe', target: str, features: list):
    input_features, output_features = [], []
    for p in features:
        if (pandas.api.types.is_numeric_dtype(df[p])):
            input_features.append({'name': p, 'type': 'numerical', 
                    'preprocessing': {'missing_value_strategy': 'fill_with_mean', 'normalization': 'zscore'}})
        elif (pandas.api.types.is_string_dtype(df[p])):
            input_features.append({'name': p, 'type': 'category'})
        else:
            raise TypeError(f'column {p} value isnt number or string')
    
    if (pandas.api.types.is_numeric_dtype(df[target])):
        output_features.append({'name': target, 'type': 'numerical', 
                    'preprocessing': {'missing_value_strategy': 'fill_with_mean', 'normalization': 'zscore'}})
    elif (pandas.api.types.is_string_dtype(df[p])):
        output_features.append({'name': target, 'type': 'category'})
    else:
        raise TypeError(f'column {target} value isnt number or string')
        
    return {
        'input_features' : input_features,
        'output_features': output_features,
    }
