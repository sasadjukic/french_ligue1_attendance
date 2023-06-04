
import pandas as pd 
from average_attendance import (
                      ajaccio_avg, angers_avg, auxerre_avg, brestois_avg, clermont_avg,
                      lens_avg, lille_avg, lorient_avg, lyonnais_avg, marseille_avg,
                      monaco_avg, montpellier_avg, nantes_avg, nice_avg, psg_avg, 
                      rennais_avg, reims_avg, strasbourg_avg, toulouse_avg, troyes_avg
                    )

ajaccio_occ = round((ajaccio_avg / 10446)*100, 2)
angers_occ = round((angers_avg / 18752)*100, 2)
auxerre_occ = round((auxerre_avg / 17924)*100, 2)
brestois_occ = round((brestois_avg / 15931)*100, 2)
clermont_occ = round((clermont_avg / 12678)*100, 2)
lens_occ = round((lens_avg / 38223)*100, 2)
lille_occ = round((lille_avg / 50186)*100, 2)
lorient_occ = round((lorient_avg / 18890)*100, 2)
lyonnais_occ = round((lyonnais_avg / 59186)*100, 2)
marseille_occ = round((marseille_avg / 67394)*100, 2)
monaco_occ = round((monaco_avg / 16500)*100, 2)
montpellier_occ = round((montpellier_avg / 22000)*100, 2)
nantes_occ = round((nantes_avg / 35332)*100, 2)
nice_occ = round((nice_avg / 36178)*100, 2)
psg_occ = round((psg_avg / 47929)*100, 2)
rennais_occ = round((rennais_avg / 29778)*100, 2)
reims_occ = round((reims_avg / 21029)*100, 2)
strasbourg_occ = round((strasbourg_avg / 26280)*100, 2)
toulouse_occ = round((toulouse_avg / 33151)*100, 2)
troyes_occ = round((troyes_avg / 20400)*100, 2)

ligue1_avg_occ = [
                  ajaccio_occ, angers_occ, auxerre_occ, brestois_occ, clermont_occ,
                  lens_occ, lille_occ, lorient_occ, lyonnais_occ, marseille_occ,
                  monaco_occ, montpellier_occ, nantes_occ, nice_occ, psg_occ,
                  rennais_occ, reims_occ, strasbourg_occ, toulouse_occ, troyes_occ
                 ]
