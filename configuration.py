from configparser import ConfigParser
import clipboard as clip

CONFIG_FILENAME = 'CONFIG.ini'
CONFIG_SECTIONS = ['[COLORS]', '[LABELS]', '[WINDOW]']
CONFIG_VARS = ['PRIMARY_COLOR', 'SECONDARY_COLOR', 'TERTIARY_COLOR', 'TEXT_COLOR', 'LABELS', 'WINDOW_SIZE']
DEF_COLORS = {'BLUE': '#0dd1da', 'GREEN': '#2fa572', 'DARK_GRAY': '#585c5c', 'LIGHT_GRAY': '#919898'}
TIME_TEST = '00:00:00 AM'
DEF_LABELS = ['Label-1:', 'Label-2:', 'Label-3:', 'Label-4:', 'Label-5:', 'Label-6:', 'Label-7:', 'Label-8:']
MLS_LABELS = ['Name:', 'Email:', 'Agent ID#:', 'Office #:', 'Address:', 'MLS#:', 'MLS#:', 'MLS#:']

PARSER = ConfigParser()


def copy_field(field):
    clip.copy(field.get())
