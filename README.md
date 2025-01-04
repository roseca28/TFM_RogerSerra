# Treball Final de Màster - Roger Serra

En aquest repositori es poden trobar els diferents scripts modificats i creats per l'execució d'aquest projecte que poden ser públics i que no pertanyen a cap altre projecte, així com aquelles dades que es poden publicar.

## Resum treball

S'ha demostrat que l'àmbit de la Intel·ligència Artificial, tot i l'avenç que suposa en l'àmbit tecnològic, comporta una elevada petjada de carboni i que, pel que fa a la sostenibilitat i a l'ecologia, implica un dels punts a millorar. És en aquest context en què, en l'àrea del Deep Learning, s'ha desenvolupat un nou modelatge conegut com a Spiking Neural Network (SNN), que suposa una reducció en les emissions de diòxid de carboni respecte a altres modelitzacions.

Aquestes són unes xarxes neuronals que es basen en el funcionament del cervell humà. A diferència de les Xarxes Neuronals Artificials (ANN), afegeixen el concepte d'spike, que és el pols elèctric encarregat de transmetre i processar informació entre les neurones.

Tot i el potencial que tenen les xarxes neuronals estudiades, gràcies a la seva capacitat de processament d'informació temporal, baix consum d'energia i alta versemblança biològica, aquestes presenten encara moltes àrees de millora.

Partint d’aquí, es pretén obtenir un entrenament de les SNN basat en aprenentatge supervisat mitjançant el descens del gradient que resolgui les problemàtiques de diferenciabilitat que presenta el seu ús, ja que el senyal dels spikes no és diferenciable. A més, corregint-ho es vol aconseguir també augmentar el rendiment de les SNN en conjunts de dades a gran escala.

Per aconseguir-ho, es realitzarà un desenvolupament teòric al voltant de la problemàtica estudiada amb la finalitat d’obtenir una metodologia per l’entrenament i, posteriorment, dur a terme una aplicació d’aquest en un conjunt de dades per observar-ne l’aplicabilitat i el rendiment.

La proposta que es presenta en aquest projecte millora els resultats que s'obtenien amb el gradient substitut original: redueix el valor de la funció de pèrdua i, en termes de sostenibilitat, s'aconsegueix una disminució en la taxa d'emissions de diòxid de carboni.
