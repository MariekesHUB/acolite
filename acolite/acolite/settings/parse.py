## def parse
## parses acolite settings files and merges with defaults
## written by Quinten Vanhellemont, RBINS
## 2021-03-09
## modifications:


def parse(sensor, settings=None):

    import os, time
    import numpy as np
    import scipy.ndimage
    import acolite as ac

    ## read default settings for sensor
    setu = ac.acolite.settings.load(sensor)

    ## add user settings
    if settings is not None:
        if type(settings) is str:
            sets = ac.acolite.settings.read(settings)
            for k in sets: setu[k] = sets[k]
        elif type(settings) is dict:
            for k in settings: setu[k] = settings[k]

    ## convert values from settings file into numbers
    int_list = ['s2_target_res', 'map_max_dim',
              'dsf_filter_box', 'dsf_tile_dimensions', 'dsf_intercept_pixels', 'dsf_smooth_box',
              'blackfill_wave', 'l2w_mask_wave', 'l2w_mask_cirrus_wave', 'glint_mask_rhos_wave', 'exp_wave1',  'exp_wave2',
              'l2w_mask_smooth_sigma',
              'flag_exponent_swir', 'flag_exponent_cirrus','flag_exponent_toa','flag_exponent_negative',
              'rgb_red_wl','rgb_green_wl', 'rgb_blue_wl',
              'dsf_wave_range', 'l2w_mask_negative_wave_range']

    float_list = ['min_tgas_aot', 'min_tgas_rho',

                  'dsf_percentile', 'dsf_filter_percentile', 'dsf_min_tile_aot', 'dsf_min_tile_cover',

                  'exp_swir_threshold', 'exp_fixed_epsilon_percentile', 'exp_fixed_aerosol_reflectance_percentile',

                  'dem_pressure_percentile', 'uoz_default', 'uwv_default', 'wind',
                  'l2w_nc_scaled_offset', 'l2w_nc_scaled_factor',

                  'blackfill_max', 'glint_mask_rhos_threshold',
                  'l2w_mask_threshold', 'l2w_mask_cirrus_threshold','l2w_mask_high_toa_threshold',
                  'rgb_min', 'rgb_max', 'gains_toa']

    ## convert values to numbers
    for k in setu:
        if k not in setu: continue
        if setu[k] is None: continue

        if type(setu[k]) is list:
            if k in int_list: setu[k] = [int(i) for i in setu[k]]
            if k in float_list: setu[k] = [float(i) for i in setu[k]]
        else:
            if k in int_list: setu[k] = int(setu[k])
            if k in float_list: setu[k] = float(setu[k])

    ## default pressure
    setu['pressure'] = 1013.25 if setu['pressure'] is None else float(setu['pressure'])

    return(setu)
