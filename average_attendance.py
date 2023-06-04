
import pandas as pd 
from l1_data import (
                      ajaccio, angers, auxerre, brestois, clermont,
                      lens, lille, lorient, lyonnais, marseille,
                      monaco, montpellier, nantes, nice, psg, 
                      rennais, reims, strasbourg, toulouse, troyes
                    )

ajaccio_avg = round(ajaccio['attendance'].mean())
angers_avg = round(angers['attendance'].mean())
auxerre_avg = round(auxerre['attendance'].mean())
brestois_avg = round(brestois['attendance'].mean())
clermont_avg = round(clermont['attendance'].mean())
lens_avg = round(lens['attendance'].mean())
lille_avg = round(lille['attendance'].mean())
lorient_avg = round(lorient['attendance'].mean())
lyonnais_avg = round(lyonnais['attendance'].mean())
marseille_avg = round(marseille['attendance'].mean())
monaco_avg = round(monaco['attendance'].mean())
montpellier_avg = round(montpellier['attendance'].mean())
nantes_avg = round(nantes['attendance'].mean())
nice_avg = round(nice['attendance'].mean())
psg_avg = round(psg['attendance'].mean())
rennais_avg = round(rennais['attendance'].mean())
reims_avg = round(reims['attendance'].mean())
strasbourg_avg = round(strasbourg['attendance'].mean())
toulouse_avg = round(toulouse['attendance'].mean())
troyes_avg = round(troyes['attendance'].mean())

ligue1_avg_att = [
                  ajaccio_avg, angers_avg, auxerre_avg, brestois_avg, clermont_avg,
                  lens_avg, lille_avg, lorient_avg, lyonnais_avg, marseille_avg,
                  monaco_avg, montpellier_avg, nantes_avg, nice_avg, psg_avg,
                  rennais_avg, reims_avg, strasbourg_avg, toulouse_avg, troyes_avg
                 ]
