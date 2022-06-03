#!/usr/bin/env python3

import os
import sys
import shutil
import zipfile
import argparse

# Das ist so besser als vorher (denke ich zumindest :-)
EXERCISE_MIN = 1
EXERCISE_MAX = 7
SEMESTER_TAG = '_wpsose21'

def getStudentInformation():
  try:
    configFile = open('projects.config', 'r', encoding='utf_8')
    content = configFile.readlines()
    contentStripped = []
    studentData = {}
    for line in content:
      line = line.strip().strip('\r\n')
      if len(line) != 0 and line[0] != '#':
        commentPos = line.find('#')
        if commentPos != -1:
          line = line[:commentPos]
        contentStripped.append(line)
        data = line.split('=')
        studentData[data[0].strip()] = data[1].strip().strip('"')
    configFile.close()
    for v in studentData.values():
      if v in ['Foo Bar', '123456', 'foobar4567']:
        sys.exit(-1)
    return studentData
  except SystemExit:
    print('\nFehler - bitte passen Sie die Datei "projects.config" an!\n')
    sys.exit(-1)
  except OSError as err:
    print("\nFehler - Datei kann nicht geoeffnet werden (" + err.strerror + ")\n")
    sys.exit(-1)
  except:
    print("\nParserfehler - bitte ueberprüfen Sie die Datei 'projects.config'!\n")
    sys.exit(-1)

# Wohoo...from Stackoverflow! - jetzt mit kleineren Änderungen...
def zipdir(path, ziph, ignorebinobj):
  for root, dirs, files in os.walk(path):
    for file in files:
      if ignorebinobj:
        path_components = root.split(os.path.sep)
        if 'obj' in path_components or 'bin' in path_components:
          continue
      ziph.write(os.path.join(root, file))

def main():
  cwd = os.getcwd()
  tmpdir = "_tmp"
  if os.path.exists(os.path.join(cwd, tmpdir)):
    print("\nSystemfehler: Temporaeres Verzeichnis existiert bereits (_tmp) - loeschen Sie das Verzeichis und versuchen Sie es erneut!")
    sys.exit(-1)

  helptext = """
             Das Aufgabenverzeichnis, für das Sie eine Abgabe erstellen wollen. Hinweis: das Skript verarbeitet nur
             relative Pfade zum Arbeitsverzeichnis. Vollstaendige Pfadangaben funktionieren nicht.
             """
  p = argparse.ArgumentParser(description='Abgabe für das Web-Programmierung-Praktikum vorbereiten.')
  p.add_argument('directory', help=helptext)

  args = p.parse_args()

  try:
    aDir = args.directory.rstrip("/")
    aDirN = int(aDir[-1])
    if (aDirN < EXERCISE_MIN or aDirN > EXERCISE_MAX) \
       or (aDirN >= EXERCISE_MIN and aDirN <= EXERCISE_MAX \
           and not os.path.exists(os.path.join(cwd, aDir))):
      print('\nFehler: Das angegebene Verzeichnis ist kein gueltiges Aufgabenverzeichnis!\n')
      sys.exit(-1)

    info = getStudentInformation()

    dirname =  info['Login'] + '_a' + str(aDirN) + SEMESTER_TAG
    if (os.path.exists(os.path.join(cwd, dirname+'.zip'))):
      sys.exit(-1)
    tmpdirFull = os.path.join(cwd, tmpdir)
    os.mkdir(tmpdirFull) # create _tmp
    submissiondir = os.path.join(tmpdirFull, dirname)
    shutil.copytree(os.path.join(cwd, aDir), submissiondir)
    shutil.copy(os.path.join(cwd, 'projects.config'), submissiondir)

    os.chdir(tmpdirFull)
    ignorebinobj = False
    if aDirN == 3:
      ignorebinobj = True
      print("")
      print("HINWEIS: ")
      print("Fuer Aufgabe 3 werden die Unterverzeichnisse 'obj' und 'bin' ignoriert und nicht mit in die ZIP-Datei gepackt!")
      print("Diese Verzeichnisse sollten nur (Neben-)Produkte des Erstellungsvorgangs enthalten und sind daher fuer die Bewertung unerheblich.")
      print("")

    zipFile = zipfile.ZipFile(dirname + '.zip', compression=zipfile.ZIP_DEFLATED, mode='w')
    zipdir(dirname, zipFile, ignorebinobj)
    zipFile.close()
    shutil.copy(os.path.join(tmpdirFull, dirname + '.zip'), cwd)
    os.chdir(cwd)
    shutil.rmtree(tmpdirFull)

    print('\nAbgabedatei ' + dirname + '.zip erfolgreich erzeugt!')
    print('Bitte entpacken Sie die Datei und ueberprüfen Sie ihren Inhalt *** VOR *** der Abgabe!\n')

  except ValueError:
    print('\nFehler: Das angegebene Verzeichnis ist kein gueltiges Aufgabenverzeichnis!\n')
    sys.exit(-1)
  except SystemExit:
    if 'dirname' in locals():
      print('\nDie Ausgabedatei ' + dirname + '.zip existiert bereits!\n')
    sys.exit(-1)
  except:
    print('\nEs ist ein Fehler aufgetreten. Bitte pruefen Sie Ihre Dateien und Verzeichnisse!\n')
    print('\n\nSollte das Problem weiterhin bestehen, kontaktieren Sie Ihren betreuenden Professor bzw. Uebungsleiter.')
    shutil.rmtree(tmppath)
    sys.exit(-1)

if __name__ == "__main__":
  main()
