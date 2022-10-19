import { ComponentStory, ComponentMeta } from '@storybook/react'
import { Button } from '.'

export default {
  title: 'Atoms/Button',
  component: Button,
} as ComponentMeta<typeof Button>

const Template: ComponentStory<typeof Button> = (props) => (
  <Button {...props}>思い出を作る</Button>
)

export const Default = Template.bind({})
