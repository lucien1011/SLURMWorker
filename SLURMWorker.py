import os

basic_script_text_template = """#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user={email}
#SBATCH --ntasks={ntasks}
#SBATCH --mem={mem}
#SBATCH --time={time}
#SBATCH --output={output}_%j.log
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
            ):
        script_file = open(out_path,"w")
        basic_script_text = basic_script_text_template.format(
                job_name = job_name,
                email = email,
                ntasks = ntasks,
                mem = mem,
                time = time,
                output = output,
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
