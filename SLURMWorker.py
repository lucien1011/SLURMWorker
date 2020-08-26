import os

basic_job_setting_template = """
#SBATCH --job-name={job_name}
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user={email}
#SBATCH --ntasks={ntasks}
#SBATCH --cpus-per-task={n_core}
#SBATCH --mem={mem}
#SBATCH --time={time}
#SBATCH --output={output}_%j.log
"""

basic_script_text_template = """#!/bin/bash
{job_setting}
pwd; hostname; date

{commands}

date
"""

array_script_text_template = """#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user={email}
#SBATCH --ntasks={ntasks}
#SBATCH --mem={mem}
#SBATCH --time={time}
#SBATCH --array={array}
#SBATCH --output={output}.%A_%a.out
#SBATCH --error={output}.%A_%a.error
pwd; hostname; date

{commands}

date
"""

class SLURMWorker(object):
    def sbatch_submit(self,file_path):
        os.system("sbatch "+file_path)

    def make_sbatch_script(self,
            out_path,
            job_name,
            email,
            ntasks,
            mem,
            time,
            output,
            commands,
            n_core="1",
            gpu=None,
            ):
        script_file = open(out_path,"w")
        job_setting = basic_job_setting_template.format(
                job_name = job_name,
                email = email,
                ntasks = ntasks,
                mem = mem,
                time = time,
                output = output,
                n_core = n_core,
                )
        if gpu:
            job_setting += """
#SBATCH --partition=gpu
#SBATCH --gpus={gpu}
""".format(gpu=gpu)
        basic_script_text = basic_script_text_template.format(
                job_setting = job_setting,
                commands = commands,
                )
        script_file.write(basic_script_text)
        script_file.close()

    def make_array_sbatch_script(self,
            out_path,
            job_name,
            email,
            ntasks,
            mem,
            time,
            output,
            array,
            commands,
            ):
        script_file = open(out_path,"w")
        basic_script_text = array_script_text_template.format(
                job_name = job_name,
                email = email,
                ntasks = ntasks,
                mem = mem,
                time = time,
                output = output,
                array = array,
                commands = commands,
                )
        script_file.write(basic_script_text)
        script_file.close()
