import os
import sys
from glob import glob
import click
from typing import List, Optional

# to add different noises testing

@click.command()
@click.pass_context
@click.option('--outdir', type=str, help='Number of greetings.', required=True, metavar='DIR')
@click.option('--seeds', default='[0,1]', type=str,
              help='Specify desired seeds number separated by comma (,) or hyphen (-)', required=True,)
@click.option('--models-folder', help='Specify folder where models for testing', required=True,)
def run_models_testing(
	ctx: click.Context,
	models_folder: str,
	seeds: Optional[List[int]],
	outdir: str
	):
	"""Call generate.py command for same set of seeds but with different models 
	to compare more deeply models evolution during training.
	"""
	if models_folder[-1] == '/':
		models_folder = models_folder[:-1]
	models_list = glob('%s/*.pkl' % models_folder)


	if len(models_folder) == 0:
		ctx.fail('This directory \'%s\' not contain any model (*.pkl)! Aborted.' % models_folder)
	else:
		for model in models_list:
			command = 'python generate.py --outdir=%s --seeds=%s --class=1  --network=%s' % (outdir, seeds, model)
			os.system(command)

#----------------------------------------------------------------------------

if __name__ == "__main__":
    run_models_testing() 

#----------------------------------------------------------------------------
