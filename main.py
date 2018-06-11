# coding:utf-8
import sys, time

class ProgressBar():

    def __init__(self, max_steps, infoDone=None):
        self.max_steps = max_steps
        self.current_step = 0
        self.progress_width = 50
        self.current_stepnfoDone = infoDone

    def update(self, step=None):
        self.current_step = step

        num_pass = int(self.current_step * self.progress_width / self.max_steps) + 1
        num_rest = self.progress_width - num_pass 
        percent = (self.current_step+1) * 100.0 / self.max_steps 
        progress_bar = '[' + '■' * (num_pass-1) + '▶' + '-' * num_rest + ']'
        progress_bar += '%.2f' % percent + '%' 
        if self.current_step < self.max_steps - 1:
            progress_bar += '\r' 
        else:
            progress_bar += '\n' 
        sys.stdout.write(progress_bar) 
        sys.stdout.flush()
        if self.current_step >= self.max_steps:
            self.current_step = 0
            print

if __name__=='__main__':
    max_steps = 300

    progress_bar = ProgressBar(max_steps)

    for i in range(max_steps):
        progress_bar.update(i)

        # do something
        time.sleep(0.01)
    print 'Done'
