import os
import pathlib
import shutil
import subprocess
import sys

import click
import dotenv

import pyqt5_tools.badplugin
import pyqt5_tools.examplebuttonplugin
import pyqt5_tools.examples

fspath = getattr(os, 'fspath', str)


here = pathlib.Path(__file__).parent
bin = here/'Qt'/'bin'
example_path = str(
    pathlib.Path(pyqt5_tools.examplebuttonplugin.__file__).parent,
)
bad_path = str(
    pathlib.Path(pyqt5_tools.badplugin.__file__).parent,
)

def pyqt5toolsinstalluic():
    destination = bin/'bin'
    destination.mkdir(parents=True, exist_ok=True)
    there = pathlib.Path(sys.executable).parent

    shutil.copy(str(there/'pyuic5.exe'), str(destination/'uic.exe'))


def load_dotenv():
    env_path = dotenv.find_dotenv(usecwd=True)
    if len(env_path) > 0:
        os.environ['DOT_ENV_DIRECTORY'] = str(pathlib.Path(env_path).parent)
        dotenv.load_dotenv(dotenv_path=env_path, override=True)


def add_to_env_var_path_list(env, name, before, after):
    return {
        name: os.pathsep.join((
            *before,
            env.get(name, ''),
            *after
        ))
    }


def mutate_env_for_paths(env):
    env.update(add_to_env_var_path_list(
        env=env,
        name='PYTHONPATH',
        before=sys.path,
        after=[''],
    ))
    env.update(add_to_env_var_path_list(
        env=env,
        name='PATH',
        before=sys.path,
        after=[''],
    ))


def print_environment_variables(env, *variables):
    for name in variables:
        value = env.get(name)
        if value is None:
            print('{} is not set'.format(name))
        else:
            print('{}: {}'.format(name, value))


qt_debug_plugins_option = click.option(
    '--qt-debug-plugins/--no-qt-debug-plugins',
    help='Set QT_DEBUG_PLUGINS=1',
)


@click.command(
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
@click.option(
    '--widget-path',
    '-p',
    'widget_paths',
    help='Paths to be combined with PYQTDESIGNERPATH',
    type=click.Path(exists=True, file_okay=False, resolve_path=True),
    multiple=True,
)
@click.option(
    '--example-widget-path',
    help='Include the path for the pyqt5-tools example button ({})'.format(
        example_path,
    ),
    is_flag=True,
)
@click.option(
    '--designer-help',
    help='Pass through to get Designer\'s --help',
    is_flag=True,
)
@click.option(
    '--test-exception-dialog',
    help='Raise an exception to check the exception dialog functionality.',
    is_flag=True,
)
@qt_debug_plugins_option
def pyqt5designer(
        ctx,
        widget_paths,
        designer_help,
        example_widget_path,
        test_exception_dialog,
        qt_debug_plugins
):
    load_dotenv()

    extras = []
    widget_paths = list(widget_paths)

    if designer_help:
        extras.append('--help')

    if example_widget_path:
        widget_paths.append(example_path)

    if test_exception_dialog:
        widget_paths.append(bad_path)

    env = dict(os.environ)
    env.update(add_to_env_var_path_list(
        env=env,
        name='PYQTDESIGNERPATH',
        before=widget_paths,
        after=[''],
    ))

    mutate_env_for_paths(env)

    if qt_debug_plugins:
        env['QT_DEBUG_PLUGINS'] = '1'

    print_environment_variables(
        env,
        'PYQTDESIGNERPATH',
        'PYTHONPATH',
        'PATH',
        'QT_DEBUG_PLUGINS',
    )

    command = [
        str(bin / 'designer.exe'),
        *extras,
        *ctx.args,
    ]

    return subprocess.call(command, env=env)


qml2_import_path_option = click.option(
    '--qml2-import-path',
    '-p',
    'qml2_import_paths',
    help='Paths to be combined with QML2_IMPORT_PATH',
    type=click.Path(exists=True, file_okay=False, resolve_path=True),
    multiple=True,
)


def mutate_qml_path(env, paths):
    env.update(add_to_env_var_path_list(
        env=env,
        name='QML2_IMPORT_PATH',
        before=[*paths, str(here/'Qt'/'qml')],
        after=[''],
    ))


@click.command(
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
@qml2_import_path_option
@click.option(
    '--qmlscene-help',
    help='Pass through to get QML scene\'s --help',
    is_flag=True,
)
@qt_debug_plugins_option
@click.option(
    '--run-qml-example',
    help='Run the pyqt5-tools QML example',
    is_flag=True,
)
def pyqt5qmlscene(
        ctx,
        qml2_import_paths,
        qmlscene_help,
        qt_debug_plugins,
        run_qml_example,
):
    load_dotenv()
    extras = []

    if qmlscene_help:
        extras.append('--help')

    env = dict(os.environ)

    if run_qml_example:
        qml2_import_paths = qml2_import_paths + (fspath(here),)
        extras.append(fspath(
            pathlib.Path(pyqt5_tools.examples.__file__).parent/'qmlapp.qml'
        ))

    mutate_qml_path(env, paths=qml2_import_paths)
    mutate_env_for_paths(env)

    if qt_debug_plugins:
        env['QT_DEBUG_PLUGINS'] = '1'

    print_environment_variables(
        env,
        'QML2_IMPORT_PATH',
        'PYTHONPATH',
        'PATH',
        'QT_DEBUG_PLUGINS',
    )

    command = [
        str(bin / 'qmlscene.exe'),
        *extras,
        *ctx.args,
    ]

    return subprocess.call(command, env=env)


@click.command(
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
@click.pass_context
@qml2_import_path_option
@click.option(
    '--qmltestrunner-help',
    help='Pass through to get QML test runner\'s --help',
    is_flag=True,
)
@qt_debug_plugins_option
@click.option(
    '--test-qml-example',
    help='Test the pyqt5-tools QML example',
    is_flag=True,
)
def pyqt5qmltestrunner(
        ctx,
        qml2_import_paths,
        qmltestrunner_help,
        qt_debug_plugins,
        test_qml_example,
):
    load_dotenv()
    extras = []

    if qmltestrunner_help:
        extras.append('--help')

    env = dict(os.environ)

    if test_qml_example:
        qml2_import_paths = qml2_import_paths + (fspath(here),)
        extras.extend([
            '-input',
            fspath(
                pathlib.Path(pyqt5_tools.examples.__file__).parent/'qmltest.qml'
            ),
        ])

    mutate_qml_path(env, paths=qml2_import_paths)
    mutate_env_for_paths(env)

    if qt_debug_plugins:
        env['QT_DEBUG_PLUGINS'] = '1'

    print_environment_variables(
        env,
        'QML2_IMPORT_PATH',
        'PYTHONPATH',
        'PATH',
        'QT_DEBUG_PLUGINS',
    )

    command = [
        str(bin / 'qmltestrunner.exe'),
        *extras,
        *ctx.args,
    ]

    return subprocess.call(command, env=env)


# def designer():
#     load_dotenv()
#     return subprocess.call([str(here/'Qt'/'bin'/'designer.exe'), *sys.argv[1:]])
def assistant():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'assistant.exe'), *sys.argv[1:]])


def canbusutil():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'canbusutil.exe'), *sys.argv[1:]])


def designer():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'designer.exe'), *sys.argv[1:]])


def dumpcpp():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'dumpcpp.exe'), *sys.argv[1:]])


def dumpdoc():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'dumpdoc.exe'), *sys.argv[1:]])


def lconvert():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'lconvert.exe'), *sys.argv[1:]])


def linguist():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'linguist.exe'), *sys.argv[1:]])


def lprodump():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'lprodump.exe'), *sys.argv[1:]])


def lrelease_pro():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'lrelease-pro.exe'), *sys.argv[1:]])


def lrelease():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'lrelease.exe'), *sys.argv[1:]])


def lupdate_pro():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'lupdate-pro.exe'), *sys.argv[1:]])


def lupdate():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'lupdate.exe'), *sys.argv[1:]])


def pixeltool():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'pixeltool.exe'), *sys.argv[1:]])


def qdbus():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qdbus.exe'), *sys.argv[1:]])


def qdbuscpp2xml():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qdbuscpp2xml.exe'), *sys.argv[1:]])


def qdbusviewer():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qdbusviewer.exe'), *sys.argv[1:]])


def qdbusxml2cpp():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qdbusxml2cpp.exe'), *sys.argv[1:]])


def qdistancefieldgenerator():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qdistancefieldgenerator.exe'), *sys.argv[1:]])


def qdoc():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qdoc.exe'), *sys.argv[1:]])


def qgltf():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qgltf.exe'), *sys.argv[1:]])


def qhelpgenerator():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qhelpgenerator.exe'), *sys.argv[1:]])


def qlalr():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qlalr.exe'), *sys.argv[1:]])


def qml():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qml.exe'), *sys.argv[1:]])


def qmlcachegen():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qmlcachegen.exe'), *sys.argv[1:]])


def qmleasing():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qmleasing.exe'), *sys.argv[1:]])


def qmlimportscanner():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qmlimportscanner.exe'), *sys.argv[1:]])


def qmllint():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qmllint.exe'), *sys.argv[1:]])


def qmlmin():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qmlmin.exe'), *sys.argv[1:]])


def qmlplugindump():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qmlplugindump.exe'), *sys.argv[1:]])


def qmlpreview():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qmlpreview.exe'), *sys.argv[1:]])


def qmlprofiler():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qmlprofiler.exe'), *sys.argv[1:]])


def qmlscene():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qmlscene.exe'), *sys.argv[1:]])


def qmltestrunner():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qmltestrunner.exe'), *sys.argv[1:]])


def qscxmlc():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qscxmlc.exe'), *sys.argv[1:]])


def qtattributionsscanner():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qtattributionsscanner.exe'), *sys.argv[1:]])


def qtdiag():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qtdiag.exe'), *sys.argv[1:]])


def qtpaths():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qtpaths.exe'), *sys.argv[1:]])


def qtplugininfo():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qtplugininfo.exe'), *sys.argv[1:]])


def qvkgen():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qvkgen.exe'), *sys.argv[1:]])


def qwebengine_convert_dict():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'qwebengine_convert_dict.exe'), *sys.argv[1:]])


def repc():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'repc.exe'), *sys.argv[1:]])


def testcon():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'testcon.exe'), *sys.argv[1:]])


def uic():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'uic.exe'), *sys.argv[1:]])


def xmlpatterns():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'xmlpatterns.exe'), *sys.argv[1:]])


def xmlpatternsvalidator():
    load_dotenv()
    return subprocess.call([str(here/'Qt'/'bin'/'xmlpatternsvalidator.exe'), *sys.argv[1:]])


