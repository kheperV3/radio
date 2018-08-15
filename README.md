# MaRadio

MaRadio est une radio à commandes vocales basée sur SNIPS
Elle utilise un raspberry 3 et une carte audio spécifique DAC+2 haut parleurs+ micro +bouton poussoir+led (https://www.raspiaudio.com)
(elle fonctionne bien sûr avec d'autres cartes audio au prix de petites modifications)

Elle est composée des éléments suivants:
- l'application Snips "Radio draft" :
avec 4 intents :

          - time : donne l'heure     ex: "quelle heure est-il ?" etc...
 
          - setStation : sélectionne la radio  ex : "je voudrais écouter France Inter" ou "France Inter" etc...
          
          - changeVolume : modifie le volume  ex: "moins fort" ou "plus fort" ou "volume 6" etc...
          
          - stopRadio : arrête la radio (shutdown)  ex: "stop" ou "arrête" ou "stop dans 10 minutes" etc...

- le programme Python réalisant les actions correspondantes : "action-louisros.radio.py" (=> https://github.com/kheperV3/radio)
- le programme de la tache qui interprete les actions précédentes : "radio.c" (=> https://github.com/kheperV3/radioTask)

Pour mettre sur pieds l'application Snips il suffit de suivre la documentation de Snips avec résolution...

Pour compiler radio.c il faut :
- disposer de la bibliotheque vlc : libvlc-dev
- executer la commande : cc -o radio -l vlc radio.c
- placer l'executable radio dans le repertoire /home/pi

Pour assurer le lancement automatique au boot de la tache radio il faut :
- ajouter la ligne suivante dans le fichier "/etc/rc.local" (sudo nano /etc/rc.local) (avant le "exit 0"...)
      /home/pi/radio&
- rebooter

Merci....
